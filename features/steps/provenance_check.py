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

"""Integration tests related to Thamos provenance-check - using thamos library."""

import os
import requests
import time
from datetime import timedelta

from thamos.lib import provenance_check_here
from thamos.config import config

from behave import then
from behave import when


@when("thamos provenance-check is run for {provenance_check_case} asynchronously")
def step_impl(context, provenance_check_case: str):
    """Call library function from Thamos to submit analysis to Thoth."""
    project_dir = os.path.join("features", "data", "project", provenance_check_case)
    config.explicit_host = context.user_api_host

    original_dir = os.getcwd()
    try:
        os.chdir(project_dir)
        context.analysis_id = provenance_check_here(
            nowait=True,
            force=True,
        )
    finally:
        os.chdir(original_dir)

    assert context.analysis_id, "No provenance check analysis id retrieved"


@then("wait for provenance-checker to finish successfully")
def step_impl(context):
    """Wait for submitted provenance-checker to finish."""
    retries = 0
    while True:
        if retries > timedelta(minutes=15).total_seconds():
            raise RuntimeError("provenance-checker took too much time to finish")

        url = f"{context.scheme}://{context.user_api_host}/api/v1/provenance/python/{context.analysis_id}"
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

        url = f"{context.scheme}://{context.user_api_host}/api/v1/provenance/python/{context.analysis_id}/status"
        response = requests.get(url)

        status = response.json()["status"]
        assert "state" in status
        assert (
            status["state"] == "terminated"
        ), f"Check of provenance for {context.analysis_id} was not successful: {status}"
        break


@then("I should be able to retrieve provenance-checker results")
def step_impl(context):
    """Retrieve provenance checker results."""
    response = requests.get(
        f"{context.scheme}://{context.user_api_host}/api/v1/provenance/python/{context.analysis_id}"
    )
    assert response.status_code == 200, (
        f"Bad status code ({response.status_code}) when obtaining adviser "
        f"result from {context.user_api_host}: {response.text}"
    )
    context.provenance_result = response.json()


@then("I should be able to see successful results of provenance check")
def step_impl(context):
    """Check provenance-checker result."""
    assert (
        context.provenance_result["result"]["error"] is False
    ), f"Provenance check {context.analysis_id!r} was not successful"
