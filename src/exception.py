import sys
import logging
import os
from datetime import datetime

# Setup logging configuration
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.ERROR,  # Logging only errors
)


def error_message_detail(error, error_detail: sys):
    """Generates detailed error messages with filename and line number."""
    exc_type, exc_value, exc_tb = error_detail.exc_info()

    if exc_tb is not None:
        file_name = exc_tb.tb_frame.f_code.co_filename
        error_message = "Error occurred in Python script: [{0}], Line Number: [{1}], Error Message: [{2}]".format(
            file_name, exc_tb.tb_lineno, str(error)
        )
    else:
        error_message = f"Error: {str(error)} (No traceback available)"

    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

        # Log the error message
        logging.error(self.error_message)

    def __str__(self):
        return self.error_message
