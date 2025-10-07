import pytest
import os

from dotenv import load_dotenv

load_dotenv()


def pytest_configure(config):
    
    if os.getenv("MD_serial_number"):
        pytest.MD_serial_number = os.getenv("MD_serial_number")
    else:
        print("MD serial number not configured. Please check the `.env` file")

    if os.getenv("HU_serial_number"):
        pytest.HU_serial_number = os.getenv("HU_serial_number")
    else:
        print("HU serial number not configured. Please check the `.env` file")
