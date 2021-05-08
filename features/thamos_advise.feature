Feature: Running thamos advise against deployment

      @seizes_backend_namespace
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
              | flask_py38                |  LATEST                 |  3.8            |
              | flask_py39                |  LATEST                 |  3.9            |
              | rhods                     |  STABLE                 |  3.8            |

     @seizes_backend_namespace
     Scenario Outline: Run thamos advise on a Git repo
        Given deployment is accessible using HTTPS
        When clone <git_repo> with Thoth application
        Then I ask for an advise for the cloned application for runtime environment <runtime_environment>, <user_stack> user stack supplied and <static_analysis> static analysis
        Then I should be able to see results of advise in the cloned application
        Then adviser result has pinned down software stack with report

        Examples: Advise
            | git_repo                                                             | runtime_environment     | user_stack  | static_analysis |
            | https://github.com/thoth-station/elyra-aidevsecops-tutorial          | download-dataset        | with        | without         |
            | https://github.com/thoth-station/elyra-aidevsecops-tutorial          | training                | without     | with            |
            | https://github.com/thoth-station/elyra-aidevsecops-tutorial          | download-dataset        | without     | without         |
            | https://github.com/thoth-station/elyra-aidevsecops-tutorial          | training                | without     | without         |
            | https://github.com/thoth-station/elyra-aidevsecops-tutorial          | inference               | without     | without         |
            | https://github.com/aicoe-aiops/ocp-ci-analysis                       | rhel:8                  | without     | without         |
