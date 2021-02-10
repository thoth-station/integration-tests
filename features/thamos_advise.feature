Feature: Running thamos advise against deployment

    Scenario: Run a simple thamos advise for a flask application for raw HTTP connection
        Given deployment is accessible using HTTPS
        When thamos advise is run for flask_py36 for recommendation type LATEST asynchronously
        Then wait for adviser to finish successfully
        Then I should be able to retrieve adviser results
        Then adviser result has pinned down software stack with report

    Scenario: Run thamos advise for RHODS stack
        Given deployment is accessible using HTTPS
        When thamos advise is run for rhods for recommendation type STABLE asynchronously
        Then wait for adviser to finish successfully
        Then I should be able to retrieve adviser results
        Then adviser result has pinned down software stack with report
