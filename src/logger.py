import logging
import os
from datetime import datetime

LOGS_DIR = "logs"
os.makedirs(LOGS_DIR, exist_ok=True) #if it already exists then don't create else create

LOG_FILE = os.path.join(LOGS_DIR, f"log_{datetime.now().strftime('%Y-%m-%d')}.log") #file name should reflect as such log_yyy-mm-dd.log

logging.basicConfig(
    filename= LOG_FILE,
    format= '%(asctime)s - %(levelname)s %(message)s',# what should be the format of the file
    level= logging.INFO #only the info and levals above info will get shown (warning, error)
)#log is getting created time - info/warning/error - message
def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger