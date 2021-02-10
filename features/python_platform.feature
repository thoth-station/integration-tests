Feature: Querying Thoth to obtain Python platform information

    Scenario Outline: Query for available Python platforms
        Given deployment is accessible using HTTPS
        When I query Thoth User API for available platforms
        Then I should get "<platform>" in the platform listing

        Examples: Packages
            | platform     |
            | linux-x86_64 |

    Scenario: Query for metadata for different indices for TensorFlow
        Given deployment is accessible using HTTPS
        When I query Thoth User API for available platforms
        Then I should count 1 in the platform listing
