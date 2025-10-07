import pytest
import subprocess

from src.automation.util.Log import Log

class Adb:

    def __init__(self):
        log = Log()
        self.logger = log.getLogger(__name__)
    
    def execCdm(self, command, serialNumber):
        try:
            result = subprocess.run(
                ['adb', '-s', serialNumber] + command.split(),  # Split the command string into a list
                capture_output=True,      # Capture stdout and stderr
                text=True,                # Decode output as text (Python 3)
                check=True                # Raise an exception for non-zero exit codes
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Error executing ADB command: {e}")
            self.logger.error(f"Stderr: {e.stderr}")
            return None
