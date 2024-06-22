from Insurance.logger import logging
from Insurance.exception import InsuranceException
import os,sys

if __name__=="__main__":
    try:
        3/0
    except Exception as e:
        logging.info(e)
        raise InsuranceException(e,sys)