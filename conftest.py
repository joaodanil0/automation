import pytest
import os

from dotenv import load_dotenv
from src.automation.util.Log import Log

load_dotenv()


def pytest_configure(config):

    if os.getenv("LOG_LEVEL"):
        pytest.LOG_LEVEL = os.getenv("LOG_LEVEL")
    else:
        pytest.LOG_LEVEL = "INFO"
    
    log = Log()
    logger = log.getLogger(__name__)
    if os.getenv("MD_serial_number"):
        pytest.MD_serial_number = os.getenv("MD_serial_number")
        logger.debug("MD_serial_number env variables loaded!")
    else:
        logger.error("MD serial number not configured. Please check the `.env` file")

    if os.getenv("HU_serial_number"):
        pytest.HU_serial_number = os.getenv("HU_serial_number")
        logger.debug("HU_serial_number env variables loaded!")
    else:
        logger.error("HU serial number not configured. Please check the `.env` file")

    
