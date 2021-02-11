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

import requests

from behave import when
from behave import then
from hamcrest import assert_that
from hamcrest import equal_to


@when('I query Thoth User API for metadata about "{index}" "{package}" "{version}"')
def step_impl(context, index: str, package: str, version: str):
    """Retrieve metadata about Python Package."""
    params = {"index": index, "name": package, "version": version}
    url = f"{context.scheme}://{context.user_api_host}/api/v1/python/package/metadata"
    response = requests.get(url, params=params)

    assert (
        response.status_code == 200
    ), f"Bad status code ({response.status_code}) when obtaining python-package-index from {url}"

    context.result = response.json()


@then('I should get "{author}" and "{maintainer}"')
def step_impl(context, author: str, maintainer: str):
    """Verify conditions for author and maintainer."""
    assert_that(context.result["author"], equal_to(author))
    assert_that(str(context.result["maintainer"]), equal_to(maintainer))


@when('I query Thoth User API for dependencies of "{package_name}" in version "{version}" from "{index}"')
def step_impl(context, package_name: str, version: str, index: str):
    """Query Thoth for Python package dependencies."""
    url = f"{context.scheme}://{context.user_api_host}/api/v1/python/package/dependencies"
    response = requests.get(url, params={"name": package_name, "version": version, "index": index})

    assert (
        response.status_code == 200
    ), f"Bad status code ({response.status_code}) when obtaining dependencies from {url}"

    context.dependencies = response.json()


@then("I should see {dependencies} in the dependency listing")
def step_impl(context, dependencies: str):
    """Check Python package dependencies."""
    package_dependencies = list(map(str.strip, dependencies.split(",")))

    for entry in context.dependencies:
        assert "environment_marker" in entry, f"No environment marker entry in the response: {entry}"
        assert "extra" in entry, f"No 'extra' entry in the response entry: {entry}"
        assert "name" in entry, f"No package name in the response entry: {entry}"
        assert "version" in entry, f"No version in the response entry: {entry}"

    for dependency in package_dependencies:
        for entry in context.dependencies:
            if entry["name"] == dependency:
                break
        else:
            assert False, f"Dependency {dependency!r} not stated in the dependency listing"


@when('I query Thoth User API for versions of "{package_name}"')
def step_impl(context, package_name: str):
    """Query User API for versions of a package."""
    url = f"{context.scheme}://{context.user_api_host}/api/v1/python/package/versions"
    response = requests.get(
        url,
        params={
            "name": package_name,
        },
    )

    assert (
        response.status_code == 200
    ), f"Bad status code ({response.status_code}) when obtaining dependencies from {url}"

    assert "versions" in response.json(), "No version key provided in the endpoint request"
    context.package_versions = response.json()["versions"]


@then("I should see {versions} in the version listing")
def step_impl(context, versions: str):
    """Check versions available for the given package."""
    versions = list(map(str.strip, versions.split(",")))

    for entry in context.package_versions:
        assert "index_url" in entry, f"No index_url provided in {entry}"
        assert "package_name" in entry, f"No package_name provided in {entry}"
        assert "package_version" in entry, f"No package_version provided in {entry}"

    for version in versions:
        for entry in context.package_versions:
            if version == entry["package_version"]:
                break
        else:
            assert (
                False
            ), f"Version {version!r} not found in the version listing, available versions: {context.package_versions}"
