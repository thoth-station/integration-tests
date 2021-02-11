Feature: Build analysis
    Scenario Outline: Analyze a container image
        Given deployment is accessible using HTTPS
        When I trigger build analysis for a build using <base_image> as a base, <output_image> as a resulting container image with <buildlog>
        Then I should be able to access stored build logs, if provided
        And I should be able to obtain information about container image analysis for the base image, if provided
        And I should be able to obtain information about container image analysis for the output image, if provided

        Examples: Builds
            | buildlog      | base_image                                                        | output_image |
            | generic.json  | registry.access.redhat.com/ubi8/ubi-minimal:latest                | None         |
