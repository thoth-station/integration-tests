#!/usr/bin/env python3
# Thoth's integration tests
# Copyright(C) 2019 Fridolin Pokorny
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

from behave import given


@given("deployment is accessible using {scheme}")
def deployment_accessible(context, scheme):
    """Check the deployment is accessible using HTTP or HTTPS."""
    if scheme not in ("HTTPS", "HTTP"):
        raise ValueError(f"Invalid scheme {scheme!r}, has to be HTTP or HTTPS")

    context.result = {}

    context.user_api_host = os.environ["THOTH_USER_API_HOST"]

    context.management_api_secret = os.environ["THOTH_MANAGEMENT_API_SECRET"]

    context.scheme = scheme.lower()
    response = requests.get(f"{context.scheme}://{context.user_api_host}/api/v1")

    assert (
        response.status_code == 200
    ), f"Invalid response when accessing User API /api/v1 endpoint: {response.status_code!r}: {response.text}"

    assert response.text, "Empty response from server for User API /api/v1 endpoint"

    context.management_api_host = os.environ["THOTH_MANAGEMENT_API_HOST"]
    response = requests.get(f"{context.scheme}://{context.management_api_host}/api/v1")

    assert (
        response.status_code == 200
    ), f"Invalid response when accessing Management API /api/v1 endpoint: {response.status_code!r}: {response.text}"

    assert response.text, "Empty response from server for Management API /api/v1 endpoint"
