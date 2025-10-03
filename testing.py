from src.logger import get_logger
from src.custom_exception import CustomException
import sys

logger =  get_logger(__name__)

def divide_num(a,b):
    try: 
        res = a/b
        logger.info("dividing two numbers")
        return res
    except Exception as e:
        logger.error("Error occured")
        raise CustomException("Custom Error 0", sys)
    
if __name__ == "__main__":
    try:
        logger.info("Starting main program")
        divide_num(10,0)
    except CustomException as ce:
        logger.error(str(ce))