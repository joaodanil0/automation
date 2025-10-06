import pytest
from src.adb.AdbCommands import AdbCommands

def test_01():
    adbCommands = AdbCommands()
    print(adbCommands.ls(pytest.MD_serial_number))
    assert True