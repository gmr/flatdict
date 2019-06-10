#!/usr/bin/env sh
set -e
if [[ -z "${AWS_ACCESS_KEY_ID}" ]]
then
    echo "AWS_ACCESS_KEY_ID is not set, exiting"
    exit 0
fi
pip install awscli coverage codecov
mkdir coverage
aws s3 cp --recursive s3://com-gavinroy-travis/flatdict/${TRAVIS_BUILD_NUMBER}/ coverage
coverage combine
cd ..
mv coverage/.coverage .
coverage report
codecov
