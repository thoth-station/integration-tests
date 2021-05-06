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

"""Tests related to Python Thoth s2i handling."""

import requests

from behave import when
from behave import then


@when("I query for the list of available Thoth s2i container images on User API")
def step_impl(context):
    """Retrieve list of Python Package Indices known to Thoth."""
    context.result = {}
    url = f"{context.scheme}://{context.user_api_host}/api/v1/s2i/python"

    response = requests.get(url)
    assert (
        response.status_code == 200
    ), f"Bad status code ({response.status_code}) when obtaining Thoth s2i from {url}: {response.text}"

    context.result = response.json()


@then('I should get "{s2i}" Python Thoth s2i container image available in the User API response')
def step_impl(context, s2i: str):
    """Verify the given s2i is available on User API."""
    for entry in context.result["s2i"]:
        if s2i == entry["thoth_s2i_image_name"]:
            assert entry.get("thoth_s2i_image_version"), f"No version identifier found for {s2i!r} Thoth s2i"
            assert entry.get("analysis_id"), f"No container image analysis found for {s2i!r} Thoth s2i"
            thoth_s2i = f"{s2i}:v{entry['thoth_s2i_image_version']}"
            assert (
                entry["thoth_s2i"] == thoth_s2i
            ), f"Wrong full qualifier for {s2i!r}, expected {thoth_s2i} but got {entry['thoth_s2i']} instead"
            break
    else:
        assert False, f"Python Thoth s2i {s2i!r} not available in the Thoth s2i listing on User API"


@then("I should see {count} Python Thoth s2i container images available")
def step_impl(context, count: str):
    """Verify number of Thoth s2i registered."""
    assert len(context.result["s2i"]) >= int(
        count
    ), f"Expected {count} Python Thoth s2i registered, got {len(context.result['s2i'])} instead"
