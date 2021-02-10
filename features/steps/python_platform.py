#!/usr/bin/env python3
# Thoth's integration tests
# Copyright(C) 2021 Red Hat, Inc.
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

"""Python platform configured."""

import requests

from behave import when
from behave import then


@when("I query Thoth User API for available platforms")
def step_impl(context):
    """Query for available Python platforms."""
    url = f"{context.scheme}://{context.user_api_host}/api/v1/python/platform"
    response = requests.get(url)

    assert (
        response.status_code == 200
    ), f"Bad status code ({response.status_code}) when obtaining platform from {url!r}: {response.text}"
    context.result = response.json()


@then('I should get "{platform}" in the platform listing')
def step_impl(context, platform: str):
    """Verify the given platform in available in the Python platform listing."""
    assert platform in context.result["platform"], f"Platform {platform!r} not in the platform listing"


@then("I should count {count} in the platform listing")
def step_impl(context, count: str):
    """Verify number of platforms in the platform listing."""
    available_count = len(context.result["platform"])
    assert available_count == int(count), f"Number of platforms available {available_count}, expected {count}"
