Feature: Running thamos advise against deployment

    Scenario Outline: Run a simple thamos advise for a flask application for raw HTTP connection
        Given deployment is accessible using HTTPS
        When thamos advise is run for <case> for recommendation type <recommendation_type> for Python <python_version> asynchronously
        Then wait for adviser to finish successfully
        Then I should be able to retrieve adviser results
        Then adviser result has pinned down software stack with report
        Then I should be able to access adviser logs

        Examples: Advise
            | case                      |  recommendation_type    |  python_version |
            | flask_py36                |  LATEST                 |  3.6            |
            | rhods                     |  STABLE                 |  3.8            |
