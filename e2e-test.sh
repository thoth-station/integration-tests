#!/usr/bin/bash

export PIPENV_HIDE_EMOJIS=1
export PIPENV_COLORBLIND=1
export THAMOS_NO_INTERACTIVE=1
export THAMOS_NO_PROGRESSBAR=1
export THAMOS_NO_EMOJI=1

E2E_TEST_REPO="${E2E_TEST_REPO:-https://github.com/thoth-station/cve-update-job.git}"
E2E_TEST_API="${E2E_TEST_API:-test.thoth-station.ninja}"

# prepare the source
echo "preparing the source..."

cd $(mktemp --directory)

echo "cloning ${E2E_TEST_REPO}..."
git clone ${E2E_TEST_REPO} .

echo "last commit log..."
git log -1

# let's change thoth config so that we hit the preprod api
sed -i 1s,.\*,host:\ ${E2E_TEST_API}, .thoth.yaml

# and get an advise...
thamos version
thamos advise --force
thamos provenance-check --force
