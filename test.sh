#!/usr/bin/env bash

export THOTH_USER_API_HOST=${THOTH_USER_API_HOST:-test.thoth-station.ninja}
export THOTH_MANAGEMENT_API_HOST=${THOTH_MANAGEMENT_API_HOST:-management.test.thoth-station.ninja}
export THOTH_AMUN_API_HOST=${THOTH_AMUN_API_HOST:-amun-api-thoth-test-core.apps.ocp.prod.psi.redhat.com}
MAIL_REPORT=${MAIL_REPORT:-0}
NO_INSTALL=${NO_INSTALL:-0}

echo -e "------------------------------------------------------------------\n\n"
echo "> Tests are executed against User API at $THOTH_USER_API_HOST"
echo "> Tests are executed against Management API at $THOTH_MANAGEMENT_API_HOST"
echo "> Tests are executed against Amun API at $THOTH_AMUN_API_HOST"
echo -e "\n\n------------------------------------------------------------------\n\n"

export PIPENV_HIDE_EMOJIS=1
export PIPENV_COLORBLIND=1

[[ "${NO_INSTALL}" -eq "1" ]] || pipenv install --deploy

if [ "${MAIL_REPORT}" -eq "1" ]; then
    pipenv --verbose run behave --show-timings -f html -o behave-report.html $@
    echo "Sending generated report..."
    pipenv run python3 sendmail.py
else
    pipenv --verbose run behave --show-timings $@
fi
