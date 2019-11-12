"""Test configuration functions, constants variables etc."""

import os
from pathlib import Path

_TEST_DIRECTORY = Path(os.path.dirname(os.path.abspath(__file__)))
_ASSETS_DIRECTORY = _TEST_DIRECTORY.joinpath("assets")

TEST_DIRECTORY_PATH = str(_TEST_DIRECTORY)
ASSETS_DIRECTORY_PATH = str(_ASSETS_DIRECTORY)
