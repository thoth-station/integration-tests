Feature: Running Dependency Monkey

      @seizes_inspection_namespace
      Scenario Outline: Run Dependency Monkey
          Given deployment is accessible using HTTPS
          When I schedule Dependency Monkey <count> times for <case> example with dry run set to <dry_run> with predictor <predictor> and configuration <predictor_config>
          Then wait for Dependency Monkey to finish successfully
          Then I should be able to retrieve Dependency Monkey logs
          Then I should be able to retrieve Dependency Monkey report

      Examples: Dependency Monkey
            | case                | count  | dry_run | predictor  | predictor_config  |
            | simple_tensorflow   | 1      | True    | AUTO       | {}                |
            | flask               | 1      | True    | RandomWalk | {}                |
