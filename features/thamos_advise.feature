Feature: Running thamos advise against deployment

      Scenario Outline: Run thamos advise on an application stack
          Given deployment is accessible using HTTPS
          When thamos advise is run for <case> for recommendation type <recommendation_type> for Python <python_version> asynchronously
          Then wait for adviser to finish successfully
          Then I should be able to retrieve adviser results
          Then adviser result has pinned down software stack with report
          Then I should be able to access adviser logs

          Examples: Advise
              | case                      |  recommendation_type    |  python_version |
              | flask_py36                |  LATEST                 |  3.6            |
              | rhods                     |  STABLE                 |  3.8            |

     Scenario Outline: Run thamos advise on a Git repo
        Given deployment is accessible using HTTPS
        When clone <git_repo> with Thoth application
        Then I ask for an advise for the cloned application for runtime environment <runtime_environment>
        Then I should be able to see results of advise in the cloned application
        Then adviser result has pinned down software stack with report

        Examples: Advise
            | git_repo                                                             | runtime_environment     |
            | https://github.com/thoth-station/elyra-aidevsecops-tutorial          | download_dataset        |
            | https://github.com/thoth-station/elyra-aidevsecops-tutorial          | training                |
            | https://github.com/thoth-station/elyra-aidevsecops-tutorial          | test_model              |
