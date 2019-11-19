Feature: Querying Thoth for Python package metadata
    Scenario: Querying for the known Python Package Indices
        Given deployment is accessible using HTTPS
        When I query for the list of known Python Package indices,
        Then I should get a list of "2"

    Scenario Outline: Query for different indices for TensorFlow
        Given deployment is accessible using HTTPS
        And I query Thoth User API for "<index>" "<package>" "<version>"
        When I execute the query
        Then I should get "<author>" and "<maintainer>"

        Examples: Packages
            | index                                                                       | package    | version | author       | maintainer |
            | https://pypi.org/simple                                                     | tensorflow | 2.0.0   | Google Inc.  | None       |
            | https://tensorflow.pypi.thoth-station.ninja/index/manylinux2010/AVX2/simple | tensorflow | 2.0.0   | Red Hat Inc. | None       |