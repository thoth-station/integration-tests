Feature: Python Thoth s2i container images
    Scenario Outline: Querying for registered Python Thoth s2i container images on User API
        Given deployment is accessible using HTTPS
        When I query for the list of available Thoth s2i container images on User API
        Then I should get "<s2i>" Python Thoth s2i container image available in the User API response

        Examples: Indexes
            | s2i                                       |
            | quay.io/thoth-station/s2i-thoth-ubi8-py38 |
            | quay.io/thoth-station/s2i-thoth-ubi8-py36 |
            | quay.io/thoth-station/s2i-thoth-f31-py37  |
            | quay.io/thoth-station/s2i-thoth-f32-py38  |

    Scenario: Querying for number of Python Thoth s2i container images
        Given deployment is accessible using HTTPS
        When I query for the list of available Thoth s2i container images on User API
        Then I should see 4 Python Thoth s2i container images available
