import pytest
import os

from dotenv import load_dotenv

load_dotenv()


def pytest_configure(config):
    pytest.MD_serial_number = os.getenv("MD_serial_number")
    pytest.HU_serial_number = os.getenv("HU_serial_number")