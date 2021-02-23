Feature: Provenance checks of Python software stacks

    @seizes_backend_namespace
    Scenario Outline: Run provenance check for a Python software stack
        Given deployment is accessible using HTTPS
        When thamos provenance-check is run for <provenance_check_case> asynchronously
        Then wait for provenance-checker to finish successfully
        Then I should be able to retrieve provenance-checker results
        Then I should be able to see successful results of provenance check

        Examples: Provenance
            | provenance_check_case     |
            | provenance_flask          |
