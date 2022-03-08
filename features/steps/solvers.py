#!/usr/bin/env python3
# Thoth's integration tests
# Copyright(C) 2019, 2020 Red Hat, Inc.
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


"""Integration tests for Thoth deployment for solvers available."""


import requests
import re
import time
from datetime import timedelta

from behave import when, then


@when("we ask for the available runtime environments")
def step_impl(context):
    """Retrieve available runtime environments."""
    url = f"{context.scheme}://{context.user_api_host}/api/v1/python/environment"
    data = requests.get(url).json()
    context.result = data


@then("I should see {os_name} in version {os_version} running {python_version}")
def step_impl(context, os_name: str, os_version: str, python_version: str):
    """Check available environments."""
    entry = {"os_name": os_name, "os_version": os_version, "python_version": python_version}

    assert entry in context.result["environment"], context.result


@when("we ask for the available solvers")
def step_impl(context):
    """Retrieve available solvers."""
    url = f"{context.scheme}://{context.management_api_host}/api/v1/solvers"
    data = requests.get(url).json()
    available_solvers = [str(solver["solver_name"]) for solver in data["solvers"]["python"]]
    context.result["available_solvers"] = available_solvers


@then("they should include at least the minimum set of solvers")
def step_impl(context):
    """Verify all requested solvers are available."""
    available_solvers = context.result["available_solvers"]
    for a_s in available_solvers:
        assert re.match("solver-(rhel|fedora)-.*\d-py3\d", a_s)  # noqa: W605


@then("schedule solver analyses for package {package_name} with version {package_version}")
def step_impl(context, package_name, package_version):
    """Schedule solver jobs for all available solvers."""
    url = f"{context.scheme}://{context.management_api_host}/api/v1/solver/python"
    response = requests.post(
        url,
        json={"package_name": package_name, "version_specifier": "==" + package_version},
        params={"secret": context.management_api_secret},
    )

    assert response.status_code == 202, (
        f"Invalid response when scheduling analysis for the given "
        f"Python package: {response.status_code!r}: {response.text}"
    )

    context.analysis_id = response.json()["analysis_id"]


@then("wait for analyses to finish successfully")
def step_impl(context):
    """Wait for scheduled sovlers to finish."""
    for a_i in context.analysis_id:
        url = f"{context.scheme}://{context.management_api_host}/api/v1/solver/python/" + a_i + "/status"
        retries = 0
        while True:
            if retries > timedelta(minutes=5).total_seconds():
                raise RuntimeError("Solver job took too much time to finish")

            response = requests.get(url)
            assert (
                response.status_code == 200
            ), f"Bad status code ({response.status_code}) when obtaining status for analysis_id {a_i}: {response.text}"
            result = response.json()
            state = result["status"]["state"]
            if state in ["running", "pending"]:
                time.sleep(1)
                retries += 1
                continue

            assert state == "finished", f"Solver {a_i} run on {context.management_api_host} was not successful"
            break
