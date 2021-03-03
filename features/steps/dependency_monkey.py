#!/usr/bin/env python3
# Thoth's integration tests
# Copyright(C) 2021 Fridolin Pokorny
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

"""Integration tests related to Dependency Monkey."""

from datetime import timedelta
import os
import requests
import time
import yaml
import toml

from thoth.common import RuntimeEnvironment

from behave import then
from behave import when


@when(
    "I schedule Dependency Monkey {count} times for {case} example with dry run set to {dry_run} with predictor "
    "{predictor} and configuration {predictor_config}"
)
def step_impl(context, case: str, count: str, dry_run: str, predictor: str, predictor_config: str):
    """Schedule a Dependency Monkey run."""
    assert dry_run in ("True", "False"), f"dry-run accepts 'True' or 'False', got {dry_run!r} instead"

    parsed_dry_run = dry_run == "True"
    parsed_predictor_config = yaml.safe_load(predictor_config)

    project_dir = os.path.join("features", "data", "dependency_monkey", case)

    with open(os.path.join(project_dir, "Pipfile")) as case_pipfile:
        pipfile = toml.load(case_pipfile)

    with open(os.path.join(project_dir, "amun_context.json")) as amun_context_file:
        amun_context = yaml.safe_load(amun_context_file)

    with open(os.path.join(project_dir, "environment.json")) as environment_file:
        environment = yaml.safe_load(environment_file)

    with open(os.path.join(project_dir, "pipeline.yaml")) as pipeline_file:
        pipeline = yaml.safe_load(pipeline_file)

    url = f"{context.scheme}://{context.management_api_host}/api/v1/dependency-monkey/python"

    payload = {
        "context": amun_context,
        "pipeline": pipeline,
        "predictor": predictor,
        "predictor_config": parsed_predictor_config,
        "requirements": pipfile,
        "runtime_environment": environment,
    }

    response = requests.post(url, params={"dry_run": parsed_dry_run, "count": int(count)}, json=payload)

    assert (
        response.status_code == 202
    ), f"Bad HTTP status code received when scheduling Dependency Monkey ({response.status_code}): {response.text}"
    context.analysis_id = response.json()["analysis_id"]

    context.pipeline = pipeline
    context.environment = environment
    context.amun_context = amun_context
    context.pipfile = pipfile
    context.count = int(count)


@then("wait for Dependency Monkey to finish successfully")
def wait_for_dependency_monkey_to_finish(context):
    """Wait for submitted analysis to finish."""
    retries = 0
    url = (
        f"{context.scheme}://{context.management_api_host}/api/v1/dependency-monkey/"
        f"python/{context.analysis_id}/status"
    )
    while True:
        if retries > timedelta(minutes=45).total_seconds():
            raise RuntimeError("Adviser analysis took too much time to finish")

        response = requests.get(url)

        assert (
            response.status_code == 200
        ), f"Error in HTTP status code {response.status_code} for {url!r}: {response.text}"

        response_body = response.json()

        if response_body["status"]["state"] != "succeeded":
            # Not finished yet.
            time.sleep(1)
            retries += 1
            continue

        assert (
            response_body["status"]["state"] == "succeeded"
        ), f"Analysis {context.analysis_id} was not successful: {response_body}"
        break


@then("I should be able to retrieve Dependency Monkey logs")
def step_impl(context) -> None:
    """Retrieve Dependency Monkey logs."""
    url = (
        f"{context.scheme}://{context.management_api_host}/api/v1/dependency-monkey/"
        f"python/{context.analysis_id}/log"
    )

    response = requests.get(url)
    assert response.status_code == 200, f"Error in HTTP status code {response.status_code} for {url!r}: {response.text}"

    response_body = response.json()

    assert "log" in response_body, "No log provided in the response"
    assert response_body["log"], "Empty log in the log response"


@then("I should be able to retrieve Dependency Monkey report")
def step_impl(context) -> None:
    """Retrieve Dependency Monkey report."""
    url = (
        f"{context.scheme}://{context.management_api_host}/api/v1/dependency-monkey/"
        f"python/{context.analysis_id}/report"
    )

    response = requests.get(url)
    assert response.status_code == 200, f"Error in HTTP status code {response.status_code} for {url!r}: {response.text}"

    response_body = response.json()

    assert "report" in response_body, f"No report available in the response: {response_body}"
    assert "result" in response_body["report"], f"No result available in the response: {response_body}"
    assert response_body["report"]["result"]["error"] is False
    assert response_body["report"]["result"]["parameters"]["pipeline"] == context.pipeline
    assert response_body["report"]["result"]["parameters"]["requirements"] == context.pipfile
    assert (
        response_body["report"]["result"]["parameters"]["runtime_environment"]
        == RuntimeEnvironment.from_dict(context.environment).to_dict()
    )
    assert response_body["report"]["result"]["parameters"]["context"] == context.amun_context
    assert response_body["report"]["result"]["parameters"]["count"] == context.count
    assert response_body["report"]["result"]["parameters"]["predictor"] == context.predictor
    assert (response_body["report"]["result"]["parameters"]["predictor_config"] or {}) == (
        context.predictor_config or {}
    )
