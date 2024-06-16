from src.logger import logging
import sys


def error_message_detail(error, error_detail:sys):
    # exception type, exception value, and traceback object

    _ , _ , exc_tb = error_detail.exc_info()

    error_message = f"Error occured in python script name: [{exc_tb.tb_frame.f_code.co_filename}] line: [{exc_tb.tb_lineno}] error message: [{str(error)}]"

    return error_message

class CustomException(Exception):

    def __init__(self, error_message, error_detail:sys):
        self.error_message = error_message_detail(error_message, error_detail)
        super().__init__(self.error_message)

    def __str__(self):
        return self.error_message
    

if __name__ == "__main__":

    try:
        a = 1/0
    except Exception as e:
        logging.debug(e)
        raise CustomException(e, sys) from None