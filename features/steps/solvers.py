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

"""Integration tests for Thoth deployment for solvers available."""

@given(u'a set of solvers')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given a set of solvers')


@when(u'we ask if the solver is available')
def step_impl(context):
    raise NotImplementedError(u'STEP: When we ask if the solver is available')


@then(u'we should find the solver available')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then we should find the solver available')