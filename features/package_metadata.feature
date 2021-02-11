Feature: Querying Thoth for Python package metadata
    Scenario Outline: Query for metadata for different indices for TensorFlow
        Given deployment is accessible using HTTPS
        When I query Thoth User API for metadata about "<index>" "<package>" "<version>"
        Then I should get "<author>" and "<maintainer>"

        Examples: Packages
            | index                                                                       | package    | version | author       | maintainer |
            | https://pypi.org/simple                                                     | tensorflow | 2.0.0   | Google Inc.  | None       |
            | https://tensorflow.pypi.thoth-station.ninja/index/manylinux2010/AVX2/simple | tensorflow | 2.0.0   | Red Hat Inc. | None       |

    Scenario Outline: Query for package dependencies
        Given deployment is accessible using HTTPS
        When I query Thoth User API for dependencies of "<package_name>" in version "<version>" from "<index>"
        Then I should see <dependencies> in the dependency listing

        Examples: Packages
            | index                                                                       | package_name    | version | dependencies   |
            | https://pypi.org/simple                                                     | tensorflow      | 2.0.0   | numpy,absl-py  |
            | https://tensorflow.pypi.thoth-station.ninja/index/manylinux2010/AVX2/simple | tensorflow      | 2.0.0   | numpy,absl-py  |

    Scenario Outline: Query for package versions
        Given deployment is accessible using HTTPS
        When I query Thoth User API for versions of "<package_name>"
        Then I should see <versions> in the version listing

        Examples: Packages
            | package_name    | versions                    |
            | tensorflow      | 2.2.0,2.3.0                 |
            | requests        | 2.11.0,0.8.5                |
