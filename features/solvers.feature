Feature: Check for solvers available in Thoth
    Scenario: Check there are minimum solvers available in Thoth
        Given a set of solvers
            | solver_name |
            | solver-rhel-8-py36 |
            | solver-fedora-31-py37 |
            | solver-fedora-31-py38 |
        And deployment is accessible using HTTPS
        When we ask if the solver is available
        Then we should find the solver available
