import numpy as np
import pandas as pd
import os
import sys
from Insurance.config import mongo_client
from Insurance.exception import InsuranceException
from Insurance.logger import logging

DATABASE_NAME="INSURANCE" 
COLLECTION_NAME="INSURANCE_PROJECT"

def get_collection_as_dataframe(database_name:str=DATABASE_NAME,collection_name:str=COLLECTION_NAME)->pd.DataFrame:
    """
    It will get data and convert to pandas dataframe.
    
    """
    try:
        logging.info("Reading data from the mongo db server")
        data=pd.DataFrame(mongo_client[DATABASE_NAME][COLLECTION_NAME].find())
        data.reset_index(drop=True,inplace=True)

        if '_id' in data.columns:
            data.drop(columns='_id',inplace=True)
        logging.info(f"data is read and has shape {data.shape}")
        return data
    
    except Exception as e:
        raise InsuranceException(e,sys)



