import sys
from networksecurity.logging import logger

class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_details: sys):
        self.error_message = error_message
        _, _, exc_tb = error_details.exc_info()
        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename
        super().__init__(self.error_message)

    def __str__(self):
        return (
            f"Error occurred in python script: '{self.file_name}', "
            f"line number: {self.lineno}, "
            f"error message: {self.error_message}"
        )

if __name__ == '__main__':
    try:
        logger.logging.info("enter the try block")
        a = 1 / 0  # Deliberate error to trigger exception
        print("The will not be printed",a)
    except Exception as e:
        raise NetworkSecurityException(e, sys)
