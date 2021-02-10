Integration tests for Thoth
---------------------------

This repo implements integration tests which can be executed against a Thoth deployment.


Running integration tests
=========================

The integration testsuite is written in `behave <https://behave.readthedocs.io/>`_ using Gherkin language.

.. code-block:: console

  ./test.sh

The command above will trigger installation of all the necessary libraries and executing the test-suite in a virtual environment. By default, test environment is tested with integration tests. The script above can be parametrized using the following environment variables:

* THOTH_USER_API_HOST - the HOST to deployment where User API sits
* THOTH_MANAGEMENT_API_HOST - the HOST to deployment where Management API sits
* THOTH_AMUN_API_HOST - the HOST to deployment where Amun API sits
* THOTH_MANAGEMENT_API_SECRET - the secret to schedule solver analysis
* NO_INSTALL - do not install dependencies (expects that the `pipenv install` command was already issued)

Examples
========

Run integration tests against stage deployment:

.. code-block:: console

  THOTH_USER_API_HOST=stage.thoth-station.ninja THOTH_MANAGEMENT_API_HOST=management.stage.thoth-station.ninja THOTH_AMUN_API_HOST=amun.stage.thoth-station.ninja ./test.sh

Run integration tests against test deployment (default behaviour):

.. code-block:: console

  THOTH_USER_API_HOST=test.thoth-station.ninja THOTH_MANAGEMENT_API_HOST=management.test.thoth-station.ninja THOTH_AMUN_API_HOST=amun.test.thoth-station.ninja ./test.sh

If you want to run a single feature test:

.. code-block:: console

  test.sh -i <feature name>.feature
