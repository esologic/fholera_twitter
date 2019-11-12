#!/usr/bin/env bash

# Run isort - change code to make sure that python imports are properly sorted

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

cd ${DIR}/..
. venv/bin/activate

export PYTHONPATH=./

seed-isort-config --exclude=venv
isort -y
