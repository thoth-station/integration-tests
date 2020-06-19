Feature: Checking Database Status
    Scenario: Estabilishing a connection to the Database
        Given deployment is accessible using HTTPS
        When I connect to the Database
        Then I should get 'True' if database is connected
        Then I should get 'True' if schema is up-to-date
