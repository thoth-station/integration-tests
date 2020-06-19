Feature: Querying Thoth for Python package versions solved for all solvers

    Scenario: Querying for Python package versions solved
        Given a list of packages
            | package_name |
            | setuptools   |
        And number of versions for each package_name is available
        And deployment is accessible using HTTPS
        And number of solvers available is provided
        When I query for the solved packages for the package_name from PyPI in Thoth Knowledge Graph
        Then I should get the same number provided from PyPI
