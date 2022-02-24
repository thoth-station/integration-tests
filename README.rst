Integration tests for Thoth
---------------------------

This repo implements integration tests which can be executed against a Thoth deployment.


Running integration tests
=========================

The integration testsuite is written in `behave <https://behave.readthedocs.io/>`_ using Gherkin language.

.. code-block:: console

  ./app.py

The command above will trigger installation of all the necessary libraries and executing the test-suite in a virtual environment. By default, test environment is tested with integration tests. The script above can be parametrized using the following environment variables:

* ``THOTH_USER_API_HOST`` - the HOST to deployment where User API sits
* ``THOTH_MANAGEMENT_API_HOST`` - the HOST to deployment where Management API sits
* ``THOTH_AMUN_API_HOST`` - the HOST to deployment where Amun API sits
* ``THOTH_MANAGEMENT_API_SECRET`` - the secret to schedule solver analysis
* ``SEND_EMAIL`` - if set to ``1``, an e-mail report is sent with integration test results

  * ``THOTH_DEPLOYMENT_NAME`` - specifies deployment name used (shown in the subject)
  * ``THOTH_EMAIL_SMTP_SERVER`` - SMTP server to be used for sending the e-mail
  * ``THOTH_EMAIL_TO`` - e-mail recipient
  * ``THOTH_EMAIL_FROM`` - sender configuration


Examples
========

Run integration tests against stage deployment:

.. code-block:: console

  THOTH_USER_API_HOST=stage.thoth-station.ninja THOTH_MANAGEMENT_API_HOST=management.stage.thoth-station.ninja THOTH_AMUN_API_HOST=amun.stage.thoth-station.ninja ./app.py

Run integration tests against test deployment (default behaviour):

.. code-block:: console

  THOTH_USER_API_HOST=test.thoth-station.ninja THOTH_MANAGEMENT_API_HOST=management.test.thoth-station.ninja THOTH_AMUN_API_HOST=amun.test.thoth-station.ninja ./app.py

If you want to run a single feature test:

.. code-block:: console

  app.py -i <feature name>.feature

If you want to run a single scenario test:

.. code-block:: console

  app.py -i <feature name> -n '<scenario name>'
