Feature: Querying Thoth for Python package metadata
    Scenario Outline: Query for metadata for different indices for TensorFlow
        Given deployment is accessible using HTTPS
        When I query Thoth User API for metadata about "<index>" "<package>" "<version>" for "<os_name>" "<os_version>" "<python_version>"
        Then I should get "<author>" and "<maintainer>"

        Examples: Packages
            | index                                                                       | package    | version | author       | maintainer | os_name  | os_version  | python_version |
            | https://pypi.org/simple                                                     | tensorflow | 2.7.0   | Google Inc.  | None       | rhel     |   8         |  3.8           |

    Scenario Outline: Query for package dependencies
        Given deployment is accessible using HTTPS
        When I query Thoth User API for dependencies of "<package_name>" in version "<version>" from "<index>" for "<os_name>" "<os_version>" "<python_version>"
        Then I should see "<dependencies>" in the dependency listing

        Examples: Packages
            | index                                                                       | package_name    | version | dependencies   | os_name | os_version  | python_version |
            | https://pypi.org/simple                                                     | tensorflow      | 2.2.0   | scipy,mock     | rhel    |    8        | 3.8            |

    Scenario Outline: Query for package versions
        Given deployment is accessible using HTTPS
        When I query Thoth User API for versions of "<package_name>" for "<os_name>" "<os_version>" "<python_version>"
        Then I should see "<package_versions>" in the version listing

        Examples: Packages
            | package_name    | package_versions            | os_name | os_version | python_version |
            | tensorflow      | 1.10.0,0.12.1               | ubi     | 8          | 3.8            |
            | requests        | 0.14.0,0.14.1               | ubi     | 8          | 3.8            |
