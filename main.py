from Insurance.logger import logging
from Insurance.exception import InsuranceException
import os,sys
from Insurance.utils import get_collection_as_dataframe

if __name__=="__main__":
    try:
        get_collection_as_dataframe()
    except Exception as e:
        logging.info(e)
        raise InsuranceException(e,sys)