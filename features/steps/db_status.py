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

"""Thoth DB integration test for Thoth deployment."""

from thoth.storages import GraphDatabase
from behave import given, when, then

graph = GraphDatabase()


@when("I connect to the Database")
def step_impl(context):
    """Check connection to the database."""
    try:
        graph.connect()
    except Exception:
        raise AssertionError("The connection to the Database failed.")


@then("I should get 'True' if database is connected")
def step_impl(context):
    """Check connection to the database."""
    assert graph.is_connected(), "Connection to database failed."


@then("I should get 'True' if schema is up-to-date")
def step_impl(context):
    """Check if schema is  up-to-date."""
    assert graph.is_schema_up2date(), "Database schema is out of date."
