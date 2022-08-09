
## Release 0.11.3 (2022-08-09T07:00:19)
* 5db65e4 :ship: Bump up base image initialized in CI. (#332)
* e400b44 :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* 753f0e4 :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* 8239900 :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* 6907862 :ship: Bump up base image initialized in CI. (#322)
* 57cd3b9 :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* 4485c79 :ship: Bump up base image initialized in CI.
* 64bf2e0 Update OWNERS and refresh pre-commit
* 7cc3225 Increase provenance-check test time limit

## Release 0.11.2 (2022-04-12T15:46:46)
* 17d358f Attach thoth and thamos versions to tests report email
* 201e059 :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* 3a80956 :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment

## Release 0.11.1 (2022-04-06T06:52:42)
* 1dd3978 Remove count and limit parameters from advise query
* 4fa4a2f Update pre-commit config and git protocol
* 5466016 :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* ed98046 :ship: Bump up base image initialized in CI.
* de7924d :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment

## Release 0.11.0 (2022-03-09T20:06:17)
* Add my username to maintainers
* Tag solver scenario to be omitted in stage

## Release 0.10.1 (2022-03-09T06:51:16)
* Fix index used for solving a package

## Release 0.10.0 (2022-03-08T18:14:55)
* Fix scenarios related to dependency monkey
* Check available runtime environments
* Remove print statement
* Extend registered indexes
* Show inspection_id if the inspection retrieval fails

## Release 0.9.3 (2022-03-01T17:08:53)
* :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* Remove ocp-ci-analysis repo
* Provide provenance-check that results in errors

## Release 0.9.2 (2022-02-24T17:08:28)
* Add running a single test scenario to docs
* Increase dependency monkey timeout
* Use dash instead of colon in the runtime environment entry
* Add username to approvers and reviewers
* Advise can take up to 20 minutes, add some time
* :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment

## Release 0.9.1 (2022-02-21T09:45:16)
* Remove thoth_s2i variable
* Update container_images feature tests according to new content format
* :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* Fix type of assert_that argument
* :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* Fix tensorflow versions and scenario parameters
* Fix package_metadata feature
* :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* :pill: fix the container image testing
* Add thoth-station/cli-examples to integration-tests

## Release 0.9.0 (2022-01-06T08:48:49)
* :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* Update features/steps/container_images.py
* Remove TODO by using the expected Thamos' config method
* Update advise and provenance features
* Update integration tests related to package metadata
* Update scenarios related to container images
* :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* Release of version 0.8.5+build.1
* :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* Swapped tab for space
* Added ps-ip-ifd
* :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* Release of version 0.8.5
* Fix assignment of the host
* Fix wrong config in thamos advise integration test
* Release of version 0.8.4
* Let Francesco release new integration-tests
* Add integrations tests for predictive stacks
* :arrow_up: Automatic update of dependencies by Kebechet
* Release of version 0.8.3
* :arrow_up: Automatic update of dependencies by Kebechet
* Expect at least 2 Python package indexes registered
* Remove indexes removed from deployments
* :arrow_up: Automatic update of dependencies by Kebechet
* :arrow_up: Automatic update of dependencies by Kebechet (#196)
* :hatched_chick: update the prow resource limits
* added some test cases
* :arrow_up: standard updates
* always verify TLS
* Release of version 0.8.2 (#193)
* Add Harshad to the maintainers listing (#191)
* Return error message if the package resolution is not avaialable (#190)
* updated anaylsis response check scenario and fix platform scenario name (#189)
* :arrow_up: Automatic update of dependencies by Kebechet (#188)
* change the dir to runtime environment
* fix s2i image availabilty check
* :arrow_up: Automatic update of dependencies by Kebechet (#183)
* :arrow_up: Automatic update of dependencies by Kebechet (#180)
* :arrow_up: Automatic update of dependencies by Kebechet (#177)
* Release of version 0.8.1 (#178)
* reduce timout of some tests (#174)
* :arrow_up: update ci config
* :sparkles: add some more info based on https://github.com/thoth-station/core/blob/master/docs/TermsAndConditionsForTheScrum.md
* :arrow_up: Automatic update of dependencies by Kebechet (#172)
* Call config.reset_config() once advise is done (#154)
* :arrow_up: Automatic update of dependencies by Kebechet (#170)
* :arrow_up: Automatic update of dependencies by Kebechet (#169)
* :arrow_up: Automatic update of dependencies by Kebechet (#166)
* :arrow_up: Automatic update of dependencies by Kebechet (#164)
* Discard any previous config loaded to the current process (#162)
* Release of version 0.8.0
* Implement testing Dependency Monkey (#159)
* Add fridex to OWNERS file
* Print response text from requests to make debugging easier
* Release of version 0.7.1 (#153)
* Reset config once advise_here is done
* Adjust versions available for requests
* Be more verbose if metadata feature fails
* :arrow_up: Automatic update of dependencies by Kebechet
* Reintroduce README file in the repo
* :arrow_up: Automatic update of dependencies by Kebechet
* Add Amun inspection namespace to deployment info response
* Propagate behave exit code
* Release of version 0.7.0
* Monitor OCP CI analysis repo
* remove the run script
* use python app to copy behave report to ARTIFACT directory
* Remove test model from elyra-aidevsecops-tutorial
* Provide support for tags passed
* add script to install dependencies and run integration test
* Adjust listing of submitted advises from integration-tests
* Include integration-tests version in e-mail subject (#134)
* Use proper status response (#133)
* :arrow_up: Automatic update of dependencies by Kebechet (#127)
* :arrow_up: Automatic update of dependencies by Kebechet (#124)
* :arrow_up: Automatic update of dependencies by Kebechet (#123)
* Release of version 0.6.0 (#122)
* Send the report as attachment (#118)
* Configure advise scenario to send user stack and code analysis (#119)
* Release of version 0.5.0 (#116)
* Implement scenarios for testing an advise on a Git repo (#113)
* Release of version 0.4.0 (#112)
* Send integration-test results to aicoe-thoth-devops (#110)
* Turn integration-tests into Thoth Python s2i application (#109)
* Adjust integration tests based on adjusted responses
* Bump black version
* Provide Python version parameter to advise scenario
* Use scenario outline for similar advise tests
* Introduce scenario for provenance check
* Add tests for obtaining versions and dependencies of packages
* pre-commit related fixes
* Add tests for build analyses
* Make sure adviser logs are accessible
* Refactor integration tests for advise
* Introduce tests related to container image analysis
* Update formatting in README
* Package indexes are now tested by Package Index scenario
* Release of version 0.3.0 (#94)
* Changes required in adviser response handling (#92)
* Add testcase for RHODS stack (#91)
* Fix formatting in README
* Fix pre-commit issues (#90)
* Add scenarios related to testing Python platform listing (#87)
* Remove database status integration tests
* Remove environments scenarios
* Add scenarios related to Python s2i endpoints
* Extend Python Package index scenarios (#85)
* Enable TLS verification when running integration tests
* :arrow_up: Automatic update of dependencies by Kebechet (#84)
* Allow passing parameters to behave runs (#82)
* Implement scenario for obtaining deployment information (#83)
* Release of version 0.2.0 (#78)
* Update OWNERS
* Add version file (#75)
* Add standard Thoth GitHub templates
* :arrow_up: Automatic update of dependencies by Kebechet (#72)
* turn on JSON output for thamos
* :arrow_down: removed the files as they are no longer required
* :arrow_up: Automatic update of dependencies by kebechet. (#71)
* :arrow_up: Automatic update of dependencies by kebechet. (#69)
* Use correct attribute to reference API URL (#68)
* removed bissenbay, thanks for your contributions!
* :sparkles: do thamos provenance check
* :pushpin: Automatic update of dependency requests from 2.24.0 to 2.25.0 (#64)
* tests for solver jobs (#57)
* :pushpin: Automatic update of dependency thoth-storages from 0.26.0 to 0.26.1 (#63)
* :pushpin: Automatic update of dependency thamos from 1.2.0 to 1.3.1 (#62)
* exclude db connection checking using tags (#61)
* :pushpin: Automatic update of dependency thoth-storages from 0.25.15 to 0.26.0 (#60)
* :pushpin: Automatic update of dependency thoth-storages from 0.25.15 to 0.26.0 (#59)
* :pushpin: Automatic update of dependency thamos from 1.0.1 to 1.2.0 (#58)
* check solver names match the regular expression (#56)
* :sparkles: configure e2e tests via ENV rather than command line
* Package Indices should be atleast 2 in deployment (#54)
* Check on workflow status state
* :pushpin: Automatic update of dependency thoth-storages from 0.25.14 to 0.25.15 (#51)
* :pushpin: Automatic update of dependency thoth-storages from 0.25.10 to 0.25.14 (#49)
* :pushpin: Automatic update of dependency thamos from 1.0.0 to 1.0.1 (#48)
* :pushpin: Automatic update of dependency thoth-storages from 0.25.6 to 0.25.10 (#46)
* :pushpin: Automatic update of dependency thamos from 0.12.2 to 1.0.0 (#45)
* :pushpin: Automatic update of dependency thoth-storages from 0.25.5 to 0.25.6 (#44)
* :pushpin: Automatic update of dependency thamos from 0.12.0 to 0.12.2 (#43)
* :pushpin: Automatic update of dependency thamos from 0.11.1 to 0.12.0 (#41)
* :pushpin: Automatic update of dependency thoth-storages from 0.25.0 to 0.25.5 (#38)
* Remove limit_latest_versions
* :pushpin: Automatic update of dependency thamos from 0.10.6 to 0.11.1 (#37)
* Validate TLS endpoints
* :pushpin: Automatic update of dependency amun from 0.4.3 to 0.5.0
* :pushpin: Automatic update of dependency thoth-storages from 0.24.4 to 0.25.0
* Add THOTH_AMUN_API_HOST
* add amun features
* :cop: make pre-commit happy
* :pushpin: Automatic update of dependency thoth-storages from 0.23.2 to 0.24.4
* :pushpin: Automatic update of dependency thamos from 0.10.5 to 0.10.6
* Update OWNERS
* Create OWNERS
* :pushpin: Automatic update of dependency thoth-storages from 0.22.12 to 0.23.2
* :pushpin: Automatic update of dependency thoth-storages from 0.22.12 to 0.23.2
* :pushpin: Automatic update of dependency requests from 2.23.0 to 2.24.0
* :pushpin: Automatic update of dependency requests from 2.23.0 to 2.24.0
* :pushpin: Automatic update of dependency thamos from 0.10.2 to 0.10.5
* :pushpin: Automatic update of dependency thamos from 0.10.2 to 0.10.5
* :pushpin: Automatic update of dependency thamos from 0.10.2 to 0.10.5
* :sparkles: added a Dockerfile so that we can run this on some cluster
* :sparkles: a lot of pre-commit related reformatting, added some required ENV
* :bug: Fixed coala errors
* Merged to one scenario
* Added db connection check
* :sparkles: added F32 py37/38 solvers
* Updates
* Update README
* Add thoth config file
* Use HOST and not URL
* Adjust metadata feature
* Refactor integration_tests
* Add check for solvers number
* Correct typos
* Correct text
* Add management API URL and steps
* Adjust name to use standard of Thoth
* Add Integrations Test for Solvers
* Add payalod to get requests
* add logging
* add missing docstrings
* add docstrings
* Correct typo
* Add integration tests for solved python packages
* :green_heart:added a simple *-environments API integration test
* :green_heart: NOT trailing slash :/
* :green_heart: new integration test for '/python/package/metadata'
* relocked and added pyhamcrest
* :sparkles: minor updates
* Update .zuul.yaml
* :sparkles: job moved to zuul-jobs repository
* :sparkles: running behave test periodically now
* added vscode directory
* replicating test.sh as playbook
* using thoth-python36 nodeset to run the job
* :green_heart: added missing newline at end of playbook file
* :sparkles: created a zuul job to run the integration test script
* :green_heart: thoth-github-wip job only works on public repositories
* :green_heart: adding standard project configuration files
* :green_heart: thoth-github-wip job only works on public repositories
* :green_heart: adding standard project configuration files
* Limit number of seconds to wait for adviser analysis to finish
* Initial implementation of integration tests

## Release 0.8.5+build.1 (2021-11-24T12:50:50)
* :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* Swapped tab for space
* Added ps-ip-ifd
* :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment

## Release 0.8.5 (2021-08-25T11:31:06)
### Features
* Fix assignment of the host
### Bug Fixes
* Fix wrong config in thamos advise integration test

## Release 0.8.4 (2021-08-17T08:57:30)
### Features
* :arrow_up: Automatic update of dependencies by Kebechet
### Improvements
* Add integrations tests for predictive stacks

## Release 0.2.0 (2021-02-08T19:56:03)
### Features
* Add version file (#75)
* Add standard Thoth GitHub templates
* :arrow_up: Automatic update of dependencies by Kebechet (#72)

## Release 0.3.0 (2021-02-10T19:53:49)
### Features
* Add testcase for RHODS stack (#91)
* Fix formatting in README
* Fix pre-commit issues (#90)
* Remove database status integration tests
* Remove environments scenarios
* Add scenarios related to Python s2i endpoints
* Extend Python Package index scenarios (#85)
* :arrow_up: Automatic update of dependencies by Kebechet (#84)
* Allow passing parameters to behave runs (#82)
* Implement scenario for obtaining deployment information (#83)
### Improvements
* Add scenarios related to testing Python platform listing (#87)
* Enable TLS verification when running integration tests

## Release 0.4.0 (2021-02-12T16:39:11)
### Features
* Send integration-test results to aicoe-thoth-devops (#110)
* Turn integration-tests into Thoth Python s2i application (#109)
* Bump black version
* Provide Python version parameter to advise scenario
* Use scenario outline for similar advise tests
* Introduce scenario for provenance check
* Make sure adviser logs are accessible
* Introduce tests related to container image analysis
* Update formatting in README
* Package indexes are now tested by Package Index scenario
### Bug Fixes
* pre-commit related fixes
### Improvements
* Adjust integration tests based on adjusted responses
* Add tests for obtaining versions and dependencies of packages
* Add tests for build analyses
* Refactor integration tests for advise

## Release 0.5.0 (2021-02-13T09:57:40)
### Improvements
* Implement scenarios for testing an advise on a Git repo (#113)

## Release 0.6.0 (2021-02-16T20:14:58)
### Features
* Send the report as attachment (#118)
### Improvements
* Configure advise scenario to send user stack and code analysis (#119)

## Release 0.7.0 (2021-02-23T08:44:13)
### Features
* Monitor OCP CI analysis repo
* remove the run script
* Remove test model from elyra-aidevsecops-tutorial
* Provide support for tags passed
* Adjust listing of submitted advises from integration-tests
* Include integration-tests version in e-mail subject (#134)
* Use proper status response (#133)
* :arrow_up: Automatic update of dependencies by Kebechet (#127)
* :arrow_up: Automatic update of dependencies by Kebechet (#124)
* :arrow_up: Automatic update of dependencies by Kebechet (#123)
### Improvements
* use python app to copy behave report to ARTIFACT directory
* add script to install dependencies and run integration test

## Release 0.7.1 (2021-02-24T14:21:16)
### Features
* Reset config once advise_here is done
* Adjust versions available for requests
* Be more verbose if metadata feature fails
* :arrow_up: Automatic update of dependencies by Kebechet
* Reintroduce README file in the repo
* :arrow_up: Automatic update of dependencies by Kebechet

## Release 0.8.0 (2021-03-03T16:09:03)
### Features
* Add fridex to OWNERS file
### Improvements
* Print response text from requests to make debugging easier
### Non-functional
* Implement testing Dependency Monkey (#159)

## Release 0.8.1 (2021-04-21T15:09:55)
### Features
* :arrow_up: update ci config
* :sparkles: add some more info based on https://github.com/thoth-station/core/blob/master/docs/TermsAndConditionsForTheScrum.md
* :arrow_up: Automatic update of dependencies by Kebechet (#172)
* Call config.reset_config() once advise is done (#154)
* :arrow_up: Automatic update of dependencies by Kebechet (#170)
* :arrow_up: Automatic update of dependencies by Kebechet (#169)
* :arrow_up: Automatic update of dependencies by Kebechet (#166)
* :arrow_up: Automatic update of dependencies by Kebechet (#164)
* Discard any previous config loaded to the current process (#162)
### Improvements
* reduce timout of some tests (#174)

## Release 0.8.2 (2021-05-07T18:53:23)
### Features
* Add Harshad to the maintainers listing (#191)
* :arrow_up: Automatic update of dependencies by Kebechet (#188)
* change the dir to runtime environment
* :arrow_up: Automatic update of dependencies by Kebechet (#183)
* :arrow_up: Automatic update of dependencies by Kebechet (#180)
* :arrow_up: Automatic update of dependencies by Kebechet (#177)
### Bug Fixes
* Return error message if the package resolution is not avaialable (#190)
* updated anaylsis response check scenario and fix platform scenario name (#189)
* fix s2i image availabilty check

## Release 0.8.3 (2021-06-28T10:34:03)
### Features
* :arrow_up: Automatic update of dependencies by Kebechet
* Expect at least 2 Python package indexes registered
* :arrow_up: Automatic update of dependencies by Kebechet
* :arrow_up: Automatic update of dependencies by Kebechet (#196)
* :hatched_chick: update the prow resource limits
* always verify TLS
### Improvements
* added some test cases
* :arrow_up: standard updates
### Other
* Remove indexes removed from deployments
