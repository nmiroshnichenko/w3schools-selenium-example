import pytest

from helpers.driver_helpers import Driver


@pytest.fixture
def driver():
    return Driver
