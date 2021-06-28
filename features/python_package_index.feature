Feature: Python package index
    Scenario Outline: Querying for the known Python Package Indexes on User API
        Given deployment is accessible using HTTPS
        When I query for the list of known Python Package indexes on User API
        Then I should get "<index_url>" Python package index available in User API response

        Examples: Indexes
            | index_url                                                                   |
            | https://pypi.org/simple                                                     |
            | https://tensorflow.pypi.thoth-station.ninja/index/manylinux2010/AVX2/simple |

    Scenario: Querying for number of Python package indexes registered
        Given deployment is accessible using HTTPS
        When I query for the list of known Python Package indexes on User API
        Then I should see at least 2 Python package indexes registered

    Scenario: Querying for PyPI index on User API
        Given deployment is accessible using HTTPS
        When I query for the list of known Python Package indexes on User API
        Then I should see PyPI.org in the listing
        And only PyPI has registered correct Warehouse API URL

    Scenario: Python Package Indexes on User API should match the ones enabled on Management API
        Given deployment is accessible using HTTPS
        When I query for the list of known Python Package indexes on User API
        Then I query for the Python Package indexes on Management API
        Then Python Package indexes available on User API should match the ones enabled on Management API
