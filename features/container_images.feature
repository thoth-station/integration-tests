Feature: Thoth container images
    Scenario Outline: Querying for registered Thoth container images on User API
        Given deployment is accessible using HTTPS
        When I query for the list of available Thoth container images on User API
        Then I should get "<container_image>" Thoth container image available in the User API response

        Examples: Indexes
            | container_image                               |
            | quay.io/thoth-station/s2i-thoth-ubi8-py38     |
            | quay.io/thoth-station/s2i-tensorflow-notebook |

    Scenario: Querying for number of Thoth container images
        Given deployment is accessible using HTTPS
        When I query for the list of available Thoth container images on User API
        Then I should see 4 Thoth container images available
