Integration tests for Thoth
---------------------------

This repo implements integration tests which can be executed against a Thoth deployment.


Running integration tests
=========================

The integration testsuite is written in `behave <https://behave.readthedocs.io/>`_ using Gherkin language.

.. code-block:: console

  ./test.sh

The command above will trigger installation of all the necessary libraries and executing the test-suite in a virtual environment. By default, test environment is tested with integration tests. The script above can be parametrized using the following environment variables:

* THOTH_USER_API_URL - an URL to deployment where User API sits
* NO_INSTALL - do not install dependencies (expects that the `pipenv install` command was already issued)

Examples
========

Run integration tests against stage deployment:

.. code-block:: console

  THOTH_USER_API_URL=stage.thoth-station.ninja ./test.sh

Run integration tests against test deployment (default behaviour):

.. code-block:: console

  THOTH_USER_API_URL=test.thoth-station.ninja ./test.sh
