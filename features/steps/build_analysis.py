#!/usr/bin/env python3
# Thoth's integration tests
# Copyright(C) 2021, Fridolin Pokorny
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


"""Integration tests for Thoth's build analysis."""

import os
import json
import requests

from behave import when
from behave import then


@when(
    "I trigger build analysis for a build using {base_image} as a base, {output_image} as a resulting container image with {buildlog}"
)
def step_impl(context, base_image: str, output_image: str, buildlog: str):
    """Trigger build analysis."""
    payload = {}

    if base_image != "None":
        payload["base_image"] = base_image

    if output_image != "None":
        payload["output_image"] = output_image

    buildlog_json = None
    if buildlog:
        with open(os.path.join("features", "data", "buildlogs", buildlog)) as input_file:
            buildlog_json = json.load(input_file)
            payload["build_log"] = buildlog_json

    url = f"{context.scheme}://{context.user_api_host}/api/v1/build-analysis"
    response = requests.post(url, json=payload)

    assert (
        response.status_code == 202
    ), f"Invalid response when submitting build analysis ({response.status_code}): {response.text}"

    assert "base_image_analysis" in response.json(), "No base image analysis in the response"
    assert "output_image_analysis" in response.json(), "No output image analysis in the response"
    assert "buildlog_analysis" in response.json(), "No buildlog analysis in the response"
    assert "buildlog_document_id" in response.json(), "No buildlog document id in the response"

    context.build_analysis = response.json()
    context.buildlog = buildlog_json


@then("I should be able to access stored build logs, if provided")
def step_impl(context):
    """Access stored build logs."""
    if not context.buildlog:
        return

    url = f"{context.scheme}://{context.user_api_host}/api/v1/buildlog/{context.build_analysis['buildlog_document_id']}"
    response = requests.get(url)

    assert (
        response.status_code == 200
    ), f"Invalid response when obtaining build log ({response.status_code}): {response.text}"
    assert response.json() == context.buildlog, "Buildlog stored is not same as the buildlog sent"


@then("I should be able to obtain information about container image analysis for the base image, if provided")
def step_impl(context):
    """Access container image analysis for the base container image."""
    if not context.build_analysis["base_image_analysis"]:
        return

    url = f"{context.scheme}://{context.user_api_host}/api/v1/analyze/{context.build_analysis['base_image_analysis']['analysis_id']}"
    response = requests.get(url)

    assert response.status_code in (
        200,
        202,
    ), f"Invalid response when obtaining container image analysis ({response.status_code}): {response.text}"


@then("I should be able to obtain information about container image analysis for the output image, if provided")
def step_impl(context):
    """Access container image analysis for the output container image."""
    if not context.build_analysis["output_image_analysis"]:
        return

    url = f"{context.scheme}://{context.user_api_host}/api/v1/analyze/{context.build_analysis['output_image_analysis']['analysis_id']}"
    response = requests.get(url)

    assert response.status_code in (
        200,
        202,
    ), f"Invalid response when obtaining container image analysis ({response.status_code}): {response.text}"
