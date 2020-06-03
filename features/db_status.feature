Feature: Checking Database Status
    Scenario: Estabilishing a connection to the Database
        Given deployment is accessible using HTTPS
        When I connect to the Database 
        Then I should if connected I should get "True"

    Scenario Outline: Checking if Database schema is up to date
        Given Database is Connected 
        When I check if schema is upto date 
        Then I should get "True" if schema is up-to-date