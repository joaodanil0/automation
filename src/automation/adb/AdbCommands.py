from src.automation.adb.Adb import Adb

class AdbCommands(Adb):

    def __init__(self):
        super().__init__()
    
    def ls(self, serialNumber):
        return self.execCdm("shell ls", serialNumber)