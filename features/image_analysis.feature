Feature: Container image analysis

    @seizes_middletier_namespace
    Scenario Outline: Analyze a container image
        Given deployment is accessible using HTTPS
        When I trigger container image analysis for <container_image> with force set to <force>
        Then I wait for the container analysis to finish successfully
        Then container image analysis results are available
        And container image analysis logs are available
        Then I ask for container image <container_image> metadata
        And I should be able to query for the container image analysis by container image hash based on metadata and results match

        Examples: Containers
            | container_image                                                              | force  |
            | registry.access.redhat.com/ubi8/ubi-minimal:latest                           | 1      |
