#!/usr/bin/env sh
set -e
nosetests -x
echo "Running Flake8 tests"
flake8