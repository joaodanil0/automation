import pytest
from src.automation.adb.AdbCommands import AdbCommands
from src.automation.util.Log import Log

def test_01():
    adbCommands = AdbCommands()
    log = Log()
    logger = log.getLogger(__name__)
    logger.info(adbCommands.ls(pytest.MD_serial_number))
    assert True