#!/usr/bin/env python3
# Thoth's integration tests
# Copyright(C) 2019 Fridolin Pokorny
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""Integration tests related to Thamos advise - using thamos library."""

from datetime import timedelta
import contextlib
import os
import requests
import tempfile
import time

from thamos.config import config
from thamos.lib import advise
from thamos.lib import advise_here
from thamos.lib import get_log
import git

from behave import then
from behave import when

_RECOMMENDATION_TYPES = frozenset(
    {
        "TESTING",
        "STABLE",
        "LATEST",
        "PERFORMANCE",
        "SECURITY",
    }
)


@contextlib.contextmanager
def cwd(path):
    """Change working directory in push-pop manner."""
    work_dir = os.getcwd()
    try:
        os.chdir(path)
        yield
    finally:
        os.chdir(work_dir)


@when(
    "thamos advise is run for {case} for recommendation type {recommendation_type} for "
    "Python {python_version} asynchronously"
)
def thamos_advise(context, case: str, recommendation_type: str, python_version: str):
    """Call library function from Thamos to submit analysis to Thoth."""
    if recommendation_type not in _RECOMMENDATION_TYPES:
        assert False, f"Invalid recommendation type {recommendation_type!r}, accepted: {list(_RECOMMENDATION_TYPES)}"

    project_dir = os.path.join("features", "data", "project", case)

    with open(os.path.join(project_dir, "Pipfile")) as case_pipfile:
        pipfile = case_pipfile.read()

    pipfile_lock = ""
    pipfile_lock_path = os.path.join(project_dir, "Pipfile.lock")
    if os.path.isfile(pipfile_lock_path):
        with open(pipfile_lock_path) as case_pipfile_lock:
            pipfile_lock = case_pipfile_lock.read()

    config.explicit_host = context.user_api_host
    context.analysis_id = advise(
        pipfile=pipfile,
        pipfile_lock=pipfile_lock,
        recommendation_type=recommendation_type,
        no_static_analysis=True,
        runtime_environment={
            "name": "rhel",
            "operating_system": {"name": "rhel", "version": "8.0"},
            "python_version": python_version,
        },
        nowait=True,
        force=True,
        limit=None,
        count=1,
        debug=True,
    )


@then("wait for adviser to finish successfully")
def wait_for_adviser_to_finish(context):
    """Wait for submitted analysis to finish."""
    retries = 0
    while True:
        if retries > timedelta(minutes=15).total_seconds():
            raise RuntimeError("Adviser analysis took too much time to finish")

        url = f"{context.scheme}://{context.user_api_host}/api/v1/advise/python/{context.analysis_id}"
        response = requests.get(url)

        assert response.status_code in (
            200,
            202,
        ), f"Error in HTTP status code {response.status_code} for {url!r}: {response.text}"

        if response.status_code == 202:
            # Not finished yet.
            time.sleep(1)
            retries += 1
            continue

        url = f"{context.scheme}://{context.user_api_host}/api/v1/advise/python/{context.analysis_id}/status"
        response = requests.get(url)

        status = response.json()["status"]
        assert "state" in status
        assert status["state"] == "terminated", f"Analysis {context.analysis_id} was not successful: {status}"
        break


@then("I should be able to retrieve adviser results")
def retrieve_advise_respond(context):
    """Retrieve analysis from Thoth using User API."""
    response = requests.get(f"{context.scheme}://{context.user_api_host}/api/v1/advise/python/{context.analysis_id}")
    assert response.status_code == 200, (
        f"Bad status code ({response.status_code}) when obtaining adviser result from "
        f"{context.user_api_host}: {response.text}"
    )
    context.adviser_result = response.json()


@then("adviser result is has no error flag set")
def adviser_result_error_flag(context):
    """Check that adviser analysis has no error flag set."""
    assert (
        context.adviser_result["result"]["error"] is False
    ), f"Adviser run with id {context.analysis_id} was not successful: {context.adviser_result}"

    assert context.adviser_result["result"]["error_msg"] is None, (
        f"Adviser run with id {context.analysis_id} was has error message set: "
        f"{context.adviser_result['result']['error_msg']}"
    )


@then("adviser result has pinned down software stack with report")
def adviser_result_has_pinned_down_software_stack(context):
    """Check presence of pinned down software stack in the computed adviser result."""
    assert context.adviser_result["result"][
        "report"
    ], f"Report field holding justification is empty for analysis {context.analysis_id}"

    assert (
        len(context.adviser_result["result"]["report"]["products"]) == 1
    ), f"Report should contain one software stack recommended for analysis {context.analysis_id}"

    assert (
        "stack_info" in context.adviser_result["result"]["report"]
    ), f"Report should container stack information for {context.analysis_id}"
    assert (
        "justification" in context.adviser_result["result"]["report"]["products"][0]
    ), f"Report should contain justification for {context.analysis_id}"
    assert (
        "advised_manifest_changes" in context.adviser_result["result"]["report"]["products"][0]
    ), f"Report should contain advised manifest changes for {context.analysis_id}"
    assert (
        "advised_runtime_environment" in context.adviser_result["result"]["report"]["products"][0]
    ), f"Report should contain advised runtime environment for {context.analysis_id}"
    assert (
        "project" in context.adviser_result["result"]["report"]["products"][0]
    ), f"Report should contain project information for {context.analysis_id}"
    assert (
        "requirements" in context.adviser_result["result"]["report"]["products"][0]["project"]
    ), f"Report should contain requirements information for {context.analysis_id}"
    assert (
        "requirements_locked" in context.adviser_result["result"]["report"]["products"][0]["project"]
    ), f"Report should contain requirements_locked information for {context.analysis_id}"
    assert (
        "runtime_environment" in context.adviser_result["result"]["report"]["products"][0]["project"]
    ), f"Report should contain runtime environment information for {context.analysis_id}"
    assert (
        "score" in context.adviser_result["result"]["report"]["products"][0]
    ), f"Report should contain score information for {context.analysis_id}"


@then("I should be able to access adviser logs")
def step_impl(context):
    """Access adviser logs."""
    response = requests.get(
        f"{context.scheme}://{context.user_api_host}/api/v1/advise/python/{context.analysis_id}/log"
    )
    assert response.status_code == 200, (
        f"Bad status code ({response.status_code}) when obtaining adviser result "
        f"from {context.user_api_host}: {response.text}"
    )

    assert "log" in response.json(), f"No log information in the response: {response.json()}"
    assert response.json()["log"], "No logs available"


@when("clone {git_repo} with Thoth application")
def step_impl(context, git_repo: str):
    """Clone the given repo."""
    context.repo = git.Repo.clone_from(git_repo, tempfile.mkdtemp(), depth=1)
    assert ".thoth.yaml" in os.listdir(context.repo.working_tree_dir), "No .thoth.yaml present in the git root"


@then(
    "I ask for an advise for the cloned application for runtime environment {runtime_environment}, "
    "{user_stack} user stack supplied and {static_analysis} static analysis"
)
def step_impl(context, runtime_environment: str, user_stack: str, static_analysis: str):
    """Ask for an advise using thamos cli."""
    assert user_stack in (
        "with",
        "without",
    ), "Wrong configuration of test, user stack should be configured using 'with'/'without'"
    assert static_analysis in (
        "with",
        "without",
    ), "Wrong configuration of test, static analysis should be configured using 'with'/'without'"

    no_user_stack = user_stack == "without"
    no_static_analysis = static_analysis == "without"

    config._configuration = None  # TODO: substitute with config.reset_config() once new thamos is released
    config.explicit_host = context.user_api_host
    with cwd(context.repo.working_tree_dir):
        try:
            results = advise_here(
                runtime_environment_name=runtime_environment,
                no_static_analysis=no_static_analysis,
                no_user_stack=no_user_stack,
                force=False,
            )
        finally:
            config.reset_config()

        assert isinstance(results, tuple)

        if results[1] is True:
            with open(".thoth_last_analysis_id", "r") as f:
                analysis_id = f.readline().strip()

            assert False, f"An error was encountered during the advise:\n{get_log(analysis_id)}"

        context.adviser_result = {"result": results[0]}


@then("I should be able to see results of advise in the cloned application")
def step_impl(context):
    """Ask for results of advise."""
    raise NotImplementedError("STEP: Then I should be able to see results of advise in the cloned application")
