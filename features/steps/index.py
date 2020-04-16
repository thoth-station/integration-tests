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

"""Basic integration tests for Thoth deployment."""

import os
import requests
import urllib.parse

from behave import given, when, then
from hamcrest import assert_that, equal_to


@given('I query Thoth User API for "{index}" "{package}" "{version}"')
def step_impl(context, index: str, package: str, version: str):
    """Retrieve metadata about Python Package."""
    context.query_string = f"{context.scheme}://{context.api_url}/api/v1/python/package/metadata" + \
        f"?index={urllib.parse.quote_plus(index)}&name={package}&version={version}"


@when("I query for the list of known Python Package indices,")
def step_impl(context):
    """Retrieve list of Python Package Indices known to Thoth."""
    response = requests.get(f"{context.scheme}://{context.api_url}/api/v1/python-package-index", verify=False,)
    assert (
        response.status_code == 200
    ), f"Bad status code ({response.status_code}) when obtaining python-package-index from {context.api_url}"
    context.result = response.json()


@when("I execute the query")
def step_impl(context):
    """Execute the prepared query."""
    response = requests.get(f"{context.query_string}", verify=False,)
    assert (
        response.status_code == 200
    ), f"Bad status code ({response.status_code}) when executing the query: {context.query_string}"

    context.result = response.json()


@then('I should get "{author}" and "{maintainer}"')
def step_impl(context, author: str, maintainer: str):
    """Verify conditions for author and maintainer."""
    assert_that(context.result["author"], equal_to(author))
    assert_that(context.result["maintainer"], equal_to(maintainer))


@then('I should get a list of "{number}"')
def step_impl(context, number: int):
    """Verify correct number is retrieved."""
    assert_that(len(context.result), equal_to(int(number)))
