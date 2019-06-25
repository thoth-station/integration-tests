#!/usr/bin/env bash

THOTH_USER_API_URL=${THOTH_USER_API_URL:-test.thoth-station.ninja}

echo -e "------------------------------------------------------------------\n\n"
echo "> Tests are executed against User API at $THOTH_USER_API_URL"
echo -e "\n\n------------------------------------------------------------------\n\n"
export THOTH_USER_API_URL
[[ $NO_INSTALL -eq "1" ]] || pipenv install --deploy
pipenv run behave --show-timings
