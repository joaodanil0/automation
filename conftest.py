import pytest


def pytest_configure(config):
    pytest.MD_serialno = "test"
    pytest.HU_serialno = "test2"