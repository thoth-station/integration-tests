Feature: Check for minimum solvers available in Thoth
    Scenario: Check there are minimum solvers available in Thoth
        Given deployment is accessible using HTTPS
        When we ask for the available solvers
        Then they should include at least the minimum set of solvers
