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

"""Python Package Index handling."""

import requests

from behave import when, then

_PYPI_URL = "https://pypi.org/simple"
_WAREHOUSE_API_URL = "https://pypi.org/pypi"


@when("I query for the list of known Python Package Indexes on User API")
def step_impl(context):
    """Retrieve list of Python Package Indices known to Thoth."""
    context.result = {}
    url = f"{context.scheme}://{context.user_api_host}/api/v1/python-package-index"
    response = requests.get(url)

    assert response.status_code == 200, (
        f"Bad status code ({response.status_code}) when obtaining " f"python-package-index from {url}: {response.text}"
    )

    context.result["indexes"] = response.json()["indexes"]


@then("I query for the Python Package indexes on Management API")
def step_impl(context):
    """Retrieve list of Python Package Indices known to Thoth."""
    url = f"{context.scheme}://{context.management_api_host}/api/v1/python-package-index"
    response = requests.get(url, params={"secret": context.management_api_secret})

    assert response.status_code == 200, (
        f"Bad status code ({response.status_code}) when obtaining " f"python-package-index from {url}: {response.text}"
    )

    context.result["management_api_indexes"] = response.json()


@then("Python Package indexes available on User API should match the ones enabled on Management API")
def step_impl(context):
    """Check registered Python package indexes match the ones exposed on User API."""
    enabled = set(i["url"] for i in context.result["management_api_indexes"]["enabled"])
    diff = enabled.symmetric_difference([i["url"] for i in context.result["indexes"]])
    assert not diff, f"Exposed Python Package indexes do not match the ones enabled on Management API"


@then('I should get "{index_url}" Python package index available in User API response')
def step_impl(context, index_url: str):
    """Verify the given index is available in User API response."""
    for entry in context.result["indexes"]:
        if index_url == entry["url"]:
            assert entry["verify_ssl"] is True, f"Index {entry['url']} is registered with verify_ssl==False"
            break
    else:
        assert False, f"Python package index {index_url!r} is not available on User API"


@then("I should see {count} Python package indexes registered")
def step_impl(context, count: int):
    """Verify PyPI has correct Warehouse API URL registered."""
    assert len(context.result["indexes"]) == int(
        count
    ), f"Expected {count} Python package indexes registered, got {len(context.result['indexes'])}"


@then("I should see PyPI.org in the listing")
def step_impl(context):
    """Verify PyPI has correct Warehouse API URL registered."""
    for entry in context.result["indexes"]:
        if entry["url"] == _PYPI_URL:
            assert entry["verify_ssl"] is True, f"Index {entry['url']!r} is registered with verify_ssl==False"
            break
    else:
        assert False, f"PyPI.org package index is not registered"


@then("only PyPI has registered correct Warehouse API URL")
def step_impl(context) -> None:
    """Check only PyPI has Warehouse API URL registered."""
    for entry in context.result["indexes"]:
        if entry["url"] == _PYPI_URL:
            assert entry["warehouse_api_url"] == _WAREHOUSE_API_URL
        else:
            assert entry["warehouse_api_url"] is None, (
                f"Index {entry['url']!r} has Warehouse API URL set "
                f"to {entry['warehouse_api_url']!r} but should be set to None"
            )
