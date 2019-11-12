#! /usr/bin/env bash

# Run pylint - make sure python code is correctly styled, is able to check for things that aren't
# looked for by black.
# Will exit non-zero if there are errors or incorrectly formatted python code.

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

cd ${DIR}/..
. venv/bin/activate

# define on separate line, so 'time' bash builtin works in container
export PYTHONPATH=${DIR}

time pylint src test