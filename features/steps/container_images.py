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

"""Tests related to Thoth container images handling."""

import requests

from behave import when
from behave import then


@when("I query for the list of available Thoth container images on User API")
def step_impl(context):
    """Retrieve list of container images known to Thoth."""
    context.result = {}
    url = f"{context.scheme}://{context.user_api_host}/api/v1/container-images"

    response = requests.get(url)
    assert (
        response.status_code == 200
    ), f"Bad status code ({response.status_code}) when obtaining Thoth container images from {url}: {response.text}"

    context.result = response.json()


@then('I should get "{container_image}" Thoth container image available in the User API response')
def step_impl(context, container_image: str):
    """Verify the given container image is available on User API."""
    for entry in context.result["container_images"]:
        if container_image == entry["thoth_s2i_image_name"]:
            assert entry.get("thoth_s2i_image_version"), f"No version identifier found for {container_image!r}"
            assert entry.get(
                "analysis_id"
            ), f"No container image analysis found for {container_image!r} Thoth container images"
            thoth_s2i = f"{container_image}:v{entry['thoth_s2i_image_version']}"
            assert entry["thoth_s2i"] == thoth_s2i, (
                f"Wrong full qualifier for {container_image!r}, expected {thoth_s2i} "
                "but got {entry['thoth_s2i']} instead"
            )
            break
    else:
        assert (
            False
        ), f"Thoth container image {container_image!r} not available in the Thoth container images listing on User API"


@then("I should see {count} Thoth container images available")
def step_impl(context, count: str):
    """Verify number of Thoth container images registered."""
    assert len(context.result["container_images"]) >= int(
        count
    ), f"Expected {count} Thoth container images registered, got {len(context.result['container_images'])} instead"
