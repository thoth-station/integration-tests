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

from behave import given, when, then


@when("I query for the list of known Python Package indices,")
def step_impl(context):
    """Retrieve list of Python Package Indices known to Thoth."""
    response = requests.get(f"{context.scheme}://{context.api_url}/api/v1/python-package-index", verify=False,)
    assert (
        response.status_code == 200
    ), f"Bad status code ({response.status_code}) when obtaining python-package-index from {context.api_url}"
    context.adviser_result = response.json()


@then("I should get a list of two")
def step_impl(context):
    raise NotImplementedError("STEP: Then I should get a list of two")
