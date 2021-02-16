
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
