#!/usr/bin/env bash

# Running this script will make all code changes needed to properly style code.

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

$DIR/apply_black.sh
$DIR/apply_isort.sh
