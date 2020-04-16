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

    context.api_url = os.environ["THOTH_USER_API_URL"]
    context.scheme = scheme.lower()
    response = requests.get(f"{context.scheme}://{context.api_url}/api/v1", verify=False)

    assert (
        response.status_code == 200
    ), f"Invalid response when accessing User API /api/v1 endpoint: {response.status_code!r}"

    assert response.text, "Empty response from server for User API /api/v1 endpoint"


@when("thamos advise is run for {case} for recommendation type {recommendation_type} asynchronously")
def thamos_advise(context, case, recommendation_type):
    """Call library function from Thamos to submit analysis to Thoth."""
    if recommendation_type not in ("TESTING", "STABLE", "LATEST"):
        raise ValueError(f"Invalid recommendation type {recommendation_type}")

    with open(f"features/data/{case}/Pipfile") as case_pipfile:
        pipfile = case_pipfile.read()

    config.explicit_host = context.api_url
    config.tls_verify = False

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
        limit_latest_versions=-1,
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

        response = requests.get(
            f"{context.scheme}://{context.api_url}/api/v1/advise/python/{context.analysis_id}/status", verify=False,
        )
        assert response.status_code == 200
        exit_code = response.json()["status"]["exit_code"]

        if exit_code is None:
            # Not finished yet.
            time.sleep(1)
            retries += 1
            continue

        assert exit_code == 0, f"Analysis {context.analysis_id} run on {context.api_url} was not successful"
        break


@then("I should be able to retrieve adviser results")
def retrieve_advise_respond(context):
    """Retrieve analysis from Thoth using User API."""
    response = requests.get(
        f"{context.scheme}://{context.api_url}/api/v1/advise/python/{context.analysis_id}", verify=False,
    )
    assert (
        response.status_code == 200
    ), f"Bad status code ({response.status_code}) when obtaining adviser result from {context.api_url}"
    context.adviser_result = response.json()


@then("adviser result is has no error flag set")
def adviser_result_error_flag(context):
    """Check that adviser analysis has no error flag set."""
    assert (
        context.adviser_result["result"]["error"] is False
    ), f"Adviser run with id {context.analysis_id} was not successful: {context.adviser_result['result']['report']}"


@then("adviser result has pinned down software stack with report")
def adviser_result_has_pinned_down_software_stack(context):
    """Check presence of pinned down software stack in the computed adviser result."""
    assert context.adviser_result["result"][
        "report"
    ], f"Report field holding justification is empty for analysis {context.analysis_id}"

    assert (
        len(context.adviser_result["result"]["report"]) == 1
    ), f"Report should contain one software stack recommended for analysis {context.analysis_id}"

    assert (
        len(context.adviser_result["result"]["report"][0]) == 3
    ), f"Report should contain justification array and requirements, wrong analysis result for {context.analysis_id}"

    stack = context.adviser_result["result"]["report"][0][1]

    assert isinstance(stack, dict), (
        f"Expected a software stack, no output produced by adviser {context.analysis_id} "
        f"(field in stack result is {stack})"
    )

    assert "requirements" in stack, (
        f"No requirements available in the adviser " f"result for analysis {context.analysis_id}: {stack}"
    )
