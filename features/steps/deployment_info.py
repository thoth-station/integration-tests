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

"""Tests related to obtaining deployment information."""

import requests

from behave import then
from behave import when

_DEPLOYMENT_INFO_KEYS = frozenset(
    {
        "amun_api_url",
        "backend_namespace",
        "deployment_name",
        "frontend_namespace",
        "knowledge_graph_host",
        "middletier_namespace",
        "s3_bucket_prefix",
        "s3_endpoint_url",
        "amun_inspection_namespace",
        # "version",
    }
)


@when("I ask for the deployment information")
def step_impl(context):
    """Retrieve deployment information."""
    url = f"{context.scheme}://{context.management_api_host}/api/v1/info"
    response = requests.get(url, params={"secret": context.management_api_secret})
    response.raise_for_status()
    context.result["response"] = response.json()


@then("I should get information about deployment")
def step_impl(context):
    """Retrieve deployment information."""
    diff = set(context.result["response"].keys()).symmetric_difference(_DEPLOYMENT_INFO_KEYS)
    assert not diff, f"Missing or unknown keys in the response: {diff!r}"

    for key, value in context.result["response"].items():
        assert value, f"Value for {key!r} is empty"
