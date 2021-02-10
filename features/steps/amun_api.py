#!/usr/bin/env python3
# Thoth's integration tests
# Copyright(C) 2020 Bissenbay Dauletbayev
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

"""Amun integration tests for Thoth deployment."""

import os
import requests
import time
from datetime import timedelta

from amun.swagger_client import InspectionApi
from amun.swagger_client import InspectionSpecification
from amun.swagger_client import InspectionSpecificationBuild
from amun.swagger_client import InspectionSpecificationBuildRequests
from amun.swagger_client import InspectionSpecificationBuildRequestsHardware
from amun.swagger_client import InspectionSpecificationRun
from amun.swagger_client import InspectionSpecificationRunRequests
from amun.swagger_client import InspectionSpecificationRunRequestsHardware
from amun.swagger_client import Configuration
from amun.swagger_client import ApiClient

from amun import get_inspection_status
from amun import get_inspection_build_log

from behave import given, when, then


@given("amun service is accessible using {scheme}")
def amun_accessible(context, scheme):
    """Check amun service is accessible using HTTP or HTTPS."""
    if scheme not in ("HTTPS", "HTTP"):
        raise ValueError(f"Invalid scheme {scheme!r}, has to be HTTP or HTTPS")

    scheme = scheme.lower()
    context.amun_api_host = f"{scheme}://{os.environ['THOTH_AMUN_API_HOST']}/api/v1"
    response = requests.get(context.amun_api_host)

    assert (
        response.status_code == 200
    ), f"Invalid response when accessing Amun API /api/v1 endpoint: {response.status_code!r}"

    assert response.text, "Empty response from server for Amun API /api/v1 endpoint"


@when("an amun inspection job is scheduled")
def amun_schedule(context):
    """Schedule a test amun inspection job."""
    configuration = Configuration()
    configuration.host = context.amun_api_host
    api_client = ApiClient(configuration)
    api_instance = InspectionApi(api_client)
    specification = InspectionSpecification(
        base="registry.access.redhat.com/ubi8/python-36",
        build=InspectionSpecificationBuild(
            requests=InspectionSpecificationBuildRequests(
                cpu="1",
                hardware=InspectionSpecificationBuildRequestsHardware(
                    cpu_family=6, cpu_model=94, physical_cpus=32, processor="Intel-Xeon-Processor-Skylake-IBRS"
                ),
                memory="1Gi",
            )
        ),
        identifier="test",
        packages=["vim"],
        python_packages=["pipenv"],
        run=InspectionSpecificationRun(
            requests=InspectionSpecificationRunRequests(
                cpu="1",
                hardware=InspectionSpecificationRunRequestsHardware(
                    cpu_family=6, cpu_model=94, physical_cpus=32, processor="Intel-Xeon-Processor-Skylake-IBRS"
                ),
                memory="512Mi",
            )
        ),
        script='#!/usr/bin/bash\necho "Here should be run tests..."\n',
        update=True,
    )
    api_response = api_instance.post_inspection(specification)
    context.inspection_id = api_response.to_dict()["inspection_id"]


@then("wait for inspection to finish successfully")
def wait_for_inspection_to_finish(context):
    """Wait for scheduled inspection to finish."""
    retries = 0
    while True:
        if retries > timedelta(minutes=45).total_seconds():
            raise RuntimeError("Inspection job took too much time to finish")

        response = get_inspection_status(context.amun_api_host, context.inspection_id)
        conditions = response["workflow"].get("conditions", None)
        if conditions is None:
            time.sleep(1)
            retries += 1
            continue

        assert (
            conditions[0]["type"] == "Completed"
        ), f"Inspection {context.inspection_id} run on {context.amun_api_host} was not successful"
        break


@then("I should be able to retrieve inspection result")
def retrieve_inspection_result(context):
    """Retrieve inspection from Thoth using Amun API."""
    response = get_inspection_build_log(context.amun_api_host, context.inspection_id)
    assert response
