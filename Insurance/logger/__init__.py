import logging
from datetime import datetime
import os

LOG_DIR='Insurance_log'
CURRENT_TIME_STAMP=datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
LOG_FILE_NAME=f"{CURRENT_TIME_STAMP}.log"

os.makedirs(LOG_DIR,exist_ok=True)

LOG_FILE_PATH=os.path.join(LOG_DIR,LOG_FILE_NAME)
FORMAT = '[%(asctime)s] %(name)s - %(levelname)s - %(message)s'

logging.basicConfig(
    filename=LOG_FILE_PATH,
    filemode="w",
    format=FORMAT,
    level=logging.INFO)
