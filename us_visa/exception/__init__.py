import os
import sys
from typing import Optional
import types


def error_message_detail(error, error_detail):
    _, _, exc_tb = error_detail.exc_info()
    
    if exc_tb is not None:
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
    else:
        file_name = "Unknown"
        line_number = 0

    error_message = "Error occurred in script name: [{0}] at line number: [{1}] error message: [{2}]".format(
        file_name, line_number, str(error)
    )
    return error_message

class USVisaException(Exception):
    def __init__(self, error_message: Optional[str], error_detail) -> None:
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self) -> str:
        return self.error_message