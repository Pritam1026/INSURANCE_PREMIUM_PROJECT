
from Insurance.logger import logging
if __name__=="__main__":
    try:
        5/0
    except Exception as e:
        logging.info(e)
