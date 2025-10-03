import traceback as tb
import sys

class CustomException(Exception):

    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message) #if error message exixsts in the predefined exceptions we will show that else we will show our own message
        self.error_message = self.get_detailed_error_message(error_message, error_detail)
    
    @staticmethod# so we don't create a class to show the custom error message
    def get_detailed_error_message(error_message, error_detail:sys):

        _ , _ , exc_tb =  error_detail.exc_info() # exc_info returns 3 things we are interested in the third thing
        file_name = exc_tb.tb_frame.f_code.co_filename # name of the file where error occured
        line_number = exc_tb.tb_lineno # line number where that error occured
        
        return f"Error in {file_name}, line {line_number} : {error_message}"
    
    def __str__(self):
        return self.error_message #gives text representation for your error message