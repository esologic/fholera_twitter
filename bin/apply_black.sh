#!/usr/bin/env bash

# Run Black - change code to make sure that python code is properly formatted.

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

cd ${DIR}/..
. venv/bin/activate

LC_ALL=C.UTF-8 LANG=C.UTF-8 black . -l 100 --exclude=venv
