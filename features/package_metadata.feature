Feature: Querying Thoth for Python package metadata

    Scenario: Run a query for the known pypi
        Given deployment is accessible using HTTPS
        When I query for the list of known Python Package indices,
        Then I should get a list of two
