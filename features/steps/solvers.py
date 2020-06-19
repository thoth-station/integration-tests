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

from behave import given, when, then
from hamcrest import assert_that, has_item


@given("a minimum set of solvers requested")
def step_impl(context):
    """Take list of solvers from table."""
    context.result = {}
    requested_solvers = []
    for row in context.table:
        requested_solvers.append(row["solver_name"])
    context.result["requested_solvers"] = requested_solvers


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
    print(context.result)
    requested_solvers = context.result["requested_solvers"]
    available_solvers = context.result["available_solvers"]
    for r_s in requested_solvers:
        assert_that(available_solvers, has_item(r_s))
