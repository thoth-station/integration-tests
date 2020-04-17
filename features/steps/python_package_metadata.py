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

"""Python Package Metadata integration test for Thoth deployment."""

import os
import requests
import urllib.parse

from behave import given, when, then
from hamcrest import assert_that, equal_to


@when('I query Thoth User API for metadata about "{index}" "{package}" "{version}"')
def step_impl(context, index: str, package: str, version: str):
    """Retrieve metadata about Python Package."""
    payload = {"index": index, "name": package, "version": version}
    response = requests.get(
        f"{context.scheme}://{context.user_api_url}/api/v1/python/package/metadata",
        verify=False,
        params=payload
    )
    assert (
            response.status_code == 200
        ), f"Bad status code ({response.status_code}) when obtaining python-package-index from {context.user_api_url}"
    context.result = response.json()


@then('I should get "{author}" and "{maintainer}"')
def step_impl(context, author: str, maintainer: str):
    """Verify conditions for author and maintainer."""
    assert_that(context.result["author"], equal_to(author))
    assert_that(str(context.result["maintainer"]), equal_to(maintainer))
