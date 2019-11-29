Feature: Recording Environments

    Scenario: Have a look at the Hardware Environments recorded
        Given deployment is accessible using HTTPS
        When I query the list of "hardware" environments
        Then I should get at least one "hardware" environment

    Scenario: Have a look at the Software Environments recorded
        Given deployment is accessible using HTTPS
        When I query the list of "software" environments
        Then I should get at least one "software" environment

    Scenario: Have a look at the Runtime Environments recorded
        Given deployment is accessible using HTTPS
        When I query the list of "runtime" environments
        Then I should get at least one "runtime" environment
