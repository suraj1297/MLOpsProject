import sys


def error_message_detail(error, error_detail:sys):
    _ , _ , exc_tb = error_detail.exc_info()

    error_message = f"Error occured in python script name: [{exc_tb.tb_frame.f_code.co_filename}] line: [{exc_tb.tb_lineno}] error message: [{str(error)}]"

    return error_message

class CustomException(Exception):

    def __init__(self, error_message, error_detail:sys):
        super.__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message