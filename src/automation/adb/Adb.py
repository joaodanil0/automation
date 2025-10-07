import pytest
import subprocess

class Adb:

    def __init__(self):
        pass
    
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
            print(f"Error executing ADB command: {e}")
            print(f"Stderr: {e.stderr}")
            return None
