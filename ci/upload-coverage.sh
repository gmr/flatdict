#!/usr/bin/env sh
set -e
pip install awscli
if [ -z "${AWS_ACCESS_KEY_ID}" ]
then
    echo "AWS_ACCESS_KEY_ID is not set, exiting"
    exit 0
fi
aws s3 cp .coverage "s3://com-gavinroy-travis/flatdict/${TRAVIS_BUILD_NUMBER}/.coverage.${TRAVIS_PYTHON_VERSION}"