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

"""Basic integration tests for Thoth deployment."""

import os
import requests
import time
from datetime import timedelta

from thamos.lib import advise
from thamos.config import config

from behave import given, when, then


@given("deployment is accessible using {scheme}")
def deployment_accessible(context, scheme):
    """Check the deployment is accessible using HTTP or HTTPS."""
    if scheme not in ("HTTPS", "HTTP"):
        raise ValueError(f"Invalid scheme {scheme!r}, has to be HTTP or HTTPS")

    context.result = {}

    context.user_api_host = os.environ["THOTH_USER_API_HOST"]

    context.management_api_secret = os.environ["THOTH_MANAGEMENT_API_SECRET"]

    context.scheme = scheme.lower()
    response = requests.get(f"{context.scheme}://{context.user_api_host}/api/v1")

    assert (
        response.status_code == 200
    ), f"Invalid response when accessing User API /api/v1 endpoint: {response.status_code!r}"

    assert response.text, "Empty response from server for User API /api/v1 endpoint"

    context.management_api_host = os.environ["THOTH_MANAGEMENT_API_HOST"]
    response = requests.get(f"{context.scheme}://{context.management_api_host}/api/v1")

    assert (
        response.status_code == 200
    ), f"Invalid response when accessing Management API /api/v1 endpoint: {response.status_code!r}"

    assert response.text, "Empty response from server for Management API /api/v1 endpoint"


@when("thamos advise is run for {case} for recommendation type {recommendation_type} asynchronously")
def thamos_advise(context, case, recommendation_type):
    """Call library function from Thamos to submit analysis to Thoth."""
    if recommendation_type not in ("TESTING", "STABLE", "LATEST"):
        raise ValueError(f"Invalid recommendation type {recommendation_type}")

    with open(f"features/data/{case}/Pipfile") as case_pipfile:
        pipfile = case_pipfile.read()

    config.explicit_host = context.user_api_host
    context.analysis_id = advise(
        pipfile=pipfile,
        pipfile_lock="",
        recommendation_type=recommendation_type,
        no_static_analysis=True,
        runtime_environment={
            "name": "rhel",
            "operating_system": {"name": "rhel", "version": "8.0"},
            "python_version": "3.6",
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
        if retries > timedelta(minutes=45).total_seconds():
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
        assert "terminated" in status
        assert (
            status["terminated"]["reason"] == "Completed"
        ), f"Analysis {context.analysis_id} was not successful: {status}"
        break


@then("I should be able to retrieve adviser results")
def retrieve_advise_respond(context):
    """Retrieve analysis from Thoth using User API."""
    response = requests.get(f"{context.scheme}://{context.user_api_host}/api/v1/advise/python/{context.analysis_id}")
    assert (
        response.status_code == 200
    ), f"Bad status code ({response.status_code}) when obtaining adviser result from {context.user_api_host}"
    context.adviser_result = response.json()


@then("adviser result is has no error flag set")
def adviser_result_error_flag(context):
    """Check that adviser analysis has no error flag set."""
    assert (
        context.adviser_result["result"]["error"] is False
    ), f"Adviser run with id {context.analysis_id} was not successful: {context.adviser_result}"

    assert (
        context.adviser_result["result"]["error_msg"] is None
    ), f"Adviser run with id {context.analysis_id} was has error message set: {context.adviser_result['result']['error_msg']}"


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
