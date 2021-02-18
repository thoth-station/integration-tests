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

"""Integration tests for container image analysis."""


import requests
import time
from datetime import timedelta

from behave import when
from behave import then


@when("I trigger container image analysis for {container_image} with force set to {force}")
def step_impl(context, container_image: str, force: str):
    """Trigger a container image analysis."""
    url = f"{context.scheme}://{context.user_api_host}/api/v1/analyze"
    force_analyze = bool(int(force))

    response = requests.post(url, params={"force": force_analyze, "image": container_image})
    assert (
        response.status_code == 202
    ), f"Triggering container image analysis failed with HTTP status code {response.status_code}: {response.text}"

    context.image_analysis = response.json()
    context.analysis_id = context.image_analysis["analysis_id"]

    if force_analyze:
        assert context.image_analysis["cached"] is False, "Cached results were obtained when force flag was set"


@then("I wait for the container analysis to finish successfully")
def step_impl(context):
    """Wait for submitted container image analysis to finish successfully."""
    retries = 0
    while True:
        if retries > timedelta(minutes=45).total_seconds():
            assert False, "Container image analysis took too much time to finish"

        url = f"{context.scheme}://{context.user_api_host}/api/v1/analyze/{context.analysis_id}"
        response = requests.get(url)

        assert response.status_code in (
            200,
            202,
        ), f"Error in HTTP status code {response.status_code} for {url} : {response.text}"

        if response.status_code == 202:
            # Not finished yet.
            time.sleep(1)
            retries += 1
            continue

        url = f"{context.scheme}://{context.user_api_host}/api/v1/analyze/{context.analysis_id}/status"
        response = requests.get(url)

        status = response.json()["status"]
        assert "state" in status
        assert (
            status["state"] == "terminated"
        ), f"Container image analysis {context.analysis_id} was not successful: {status}"
        break


@then("container image analysis results are available")
def step_impl(context):
    """Container image analysis results are available."""
    url = f"{context.scheme}://{context.user_api_host}/api/v1/analyze/{context.analysis_id}"
    response = requests.get(url)

    assert (
        response.status_code == 200
    ), f"Invalid HTTP status code when obtaining results: {response.status_code}: {response.text}"
    context.analysis_result = response.json()


@then("container image analysis logs are available")
def step_impl(context):
    """Container image analysis results logs are available."""
    url = f"{context.scheme}://{context.user_api_host}/api/v1/analyze/{context.analysis_id}/log"
    response = requests.get(url)

    assert (
        response.status_code == 200
    ), f"Invalid HTTP status code when obtaining logs: {response.status_code}: {response.text}"

    assert "log" in response.json(), f"No log entry in the JSON response: {response.json()}"

    context.analysis_logs = response.json()
    assert context.analysis_logs, "Empty container image analysis logs retrieved"


@then("I ask for container image {container_image} metadata")
def step_impl(context, container_image):
    """Check metadata of a container image."""
    url = f"{context.scheme}://{context.user_api_host}/api/v1/image/metadata"
    response = requests.post(url, params={"image": container_image})

    assert (
        response.status_code == 200
    ), f"Invalid HTTP status code when obtaining container image metadata: {response.status_code}: {response.text}"

    assert response.json(), "Metadata obtained are empty"
    context.image_metadata = response.json()


@then(
    "I should be able to query for the container image analysis by "
    "container image hash based on metadata and results match"
)
def step_impl(context):
    """Check metadata of a container image."""
    assert "digest" in context.image_metadata, "No digest available in the image metadata obtained"

    url = f"{context.scheme}://{context.user_api_host}/api/v1/analyze/by-hash/{context.image_metadata['digest']}"
    response = requests.get(url)

    assert (
        response.status_code == 200
    ), f"Invalid HTTP status code when obtaining container image by hash: {response.status_code}: {response.text}"

    assert (
        response.json() == context.analysis_result
    ), "Container image results obtained do not match with the ones received by image analysis"
