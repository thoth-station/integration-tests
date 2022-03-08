Feature: Check for minimum solvers available in Thoth
    Scenario: Check there are minimum solvers available in Thoth
        Given deployment is accessible using HTTPS
        When we ask for the available solvers
        Then they should include at least the minimum set of solvers

    Scenario: Schedule solver jobs for all available solvers in Thoth
        Given deployment is accessible using HTTPS
        When we ask for the available solvers
        Then schedule solver analyses for package selinon with version 1.0.0
        Then wait for analyses to finish successfully

    Scenario Outline: Check runtime environments reported
        Given deployment is accessible using HTTPS
        When we ask for the available runtime environments
        Then I should see <os_name> in version <os_version> running <python_version>

        Examples: Runtime environments
              | os_name  | os_version  | python_version |
              |  rhel    |    8        | 3.8            |
              |  fedora  |   34        | 3.9            |
              |  ubi     |    8        | 3.8            |
