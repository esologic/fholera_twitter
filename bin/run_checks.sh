#! /usr/bin/env bash

# Run all code checks to make sure code meets formatting standards.
# Will exit non-zero if there are errors or improperly formatted code.

set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

echo "Running Pylint"
exec $DIR/run_pylint.sh

echo "Running Isort"
exec $DIR/run_isort.sh

echo "Running Black"
exec $DIR/run_black.sh

echo "Running Vulture"
exec $DIR/run_vulture.sh
