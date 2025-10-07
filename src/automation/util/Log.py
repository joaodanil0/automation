
import logging
import pytest

from io import StringIO
from rich.console import Console
from rich.logging import RichHandler

class Log:

    def __init__(self):
        self.file_handler = logging.FileHandler("logs.txt")
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.file_handler.setFormatter(formatter)
        self.rich_handler = RichHandler(
            show_time=True,
            show_level=True,
            show_path=False, # Or True, depending on your preference
            rich_tracebacks=True,
            omit_repeated_times=False
        )

    
    def getLogger(self, name):
        logger = logging.getLogger(name)
        logger.setLevel(pytest.LOG_LEVEL)
        logger.addHandler(self.rich_handler)
        logger.addHandler(self.file_handler)
        return logger