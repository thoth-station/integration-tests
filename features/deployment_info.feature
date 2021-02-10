Feature: Deployment
    Scenario: Deployment information
        Given deployment is accessible using HTTPS
        When I ask for the deployment information
        Then I should get information about deployment
