import os

from pathlib import Path

import pytest


@pytest.fixture(scope="session")
def testdata():
    try:
        return Path(os.environ["PYMSBUILD_TEST_TESTDATA"])
    except KeyError:
        return Path(__file__).absolute().parent / "testdata"
