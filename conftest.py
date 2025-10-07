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
        logger.debug("MD_serial_number env variable loaded!")
    else:
        logger.error("MD serial number not configured. Please check the `.env` file")

    if os.getenv("HU_serial_number"):
        pytest.HU_serial_number = os.getenv("HU_serial_number")
        logger.debug("HU_serial_number env variable loaded!")
    else:
        logger.error("HU serial number not configured. Please check the `.env` file")
    
    if os.getenv("APPIUM_SERVER_IP"):
        pytest.APPIUM_SERVER_IP = os.getenv("APPIUM_SERVER_IP")
        logger.debug("APPIUM_SERVER_IP env variable loaded!")
    else:
        logger.error("Appium server IP not configured. Please check the `.env` file")
    
    if os.getenv("APPIUM_SERVER_PORT"):
        pytest.APPIUM_SERVER_PORT = os.getenv("APPIUM_SERVER_PORT")
        logger.debug("APPIUM_SERVER_PORT env variable loaded!")
    else:
        logger.error("Appium server port not configured. Please check the `.env` file")

    
