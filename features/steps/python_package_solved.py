#!/usr/bin/env python3
# Thoth's integration tests
# Copyright(C) 2019 Red Hat, Inc.
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

"""Python Package solved integration tests for Thoth deployment."""

import os
import requests
import urllib.parse
import logging

from behave import given, when, then
from hamcrest import assert_that, equal_to

_LOGGER = logging.getLogger(__name__)


@given("a list of packages")
def step_impl(context):
    """Take list of python package from table."""
    context.result = {}
    for row in context.table:
        context.result[row["package_name"]] = {}


@given("number of versions for each package_name is available")
def step_impl(context):
    """Get number of versions available from PyPI for the package_name."""
    # TODO: check number of solvers
    thoth_solvers = 3
    for package in context.result.keys():
        url = "https://pypi.python.org/pypi/{}/json".format(package)
        data = requests.get(url).json()
        number_pypi = len(list(data["releases"].keys()))
        context.result[package]["number_pypi"] = number_pypi*thoth_solvers


@when("I query for the solved packages for the package_name from PyPI in Thoth Knowledge Graph")
def step_impl(context):
    """Get number of versions available from PyPI for the package_name queryin Thoth knowledge graph."""
    for package in context.result.keys():
        payload = {'name': package}
        response = requests.get(
            f"{context.scheme}://{context.api_url}/api/v1/python/packages/count", params=payload)
        context.result[package]["number_thoth"] = response.json()["count"]


@then("I should get the same number provided from PyPI")
def step_impl(context):
    """Assert that all versions from PyPI are solved inside Thoth knowledge graph."""
    _LOGGER.info(context.result)
    for package in context.result.keys():
        assert_that(context.result[package]["number_thoth"], equal_to(context.result[package]["number_pypi"]))
