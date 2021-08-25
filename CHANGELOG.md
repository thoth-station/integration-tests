
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
