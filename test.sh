#!/usr/bin/env bash

THOTH_USER_API_HOST=${THOTH_USER_API_HOST:-test.thoth-station.ninja}

echo -e "------------------------------------------------------------------\n\n"
echo "> Tests are executed against User API at $THOTH_USER_API_HOST"
echo -e "\n\n------------------------------------------------------------------\n\n"
export THOTH_USER_API_HOST
[[ $NO_INSTALL -eq "1" ]] || pipenv install --deploy
pipenv run behave --show-timings
