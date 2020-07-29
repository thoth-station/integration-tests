Feature: Aggregating Build Logs
    Scenario: Browsing logs of container images builds during Amun inspection jobs
        Given amun service is accessible using HTTP
        When an amun inspection job is scheduled
        Then wait for inspection to finish successfully
        Then I should be able to retrieve inspection result
