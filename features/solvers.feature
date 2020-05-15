Feature: Check for minimum solvers available in Thoth
    Scenario: Check there are minimum solvers available in Thoth
        Given deployment is accessible using HTTPS
        And a minimum set of solvers requested
            | solver_name |
            | solver-rhel-8-py36 |
            | solver-fedora-31-py37 |
            | solver-fedora-31-py38 |
            | solver-fedora-32-py37 |
            | solver-fedora-32-py38 |
        When we ask for the available solvers
        Then they should include at least the minimum set of solvers
