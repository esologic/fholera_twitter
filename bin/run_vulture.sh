#!/usr/bin/env bash

# Run isort in check mode to ensure that there are not outstanding changes that need to be made.
# Will exit non-zero if there are errors or incorrectly formatted python imports.

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

cd ${DIR}/..
. venv/bin/activate

export PYTHONPATH=./

# You will probably have to tune this --min-confidence as your project grows
vulture src/ test/ .vulture_ignore.py --min-confidence 60
