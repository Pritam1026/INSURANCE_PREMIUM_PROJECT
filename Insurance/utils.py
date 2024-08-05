import numpy as np
import pandas as pd
import os
import sys
from Insurance.config import mongo_client
from Insurance.exception import InsuranceException
from Insurance.logger import logging
import yaml
import dill

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



def convert_columns_float(df:pd.DataFrame,exclude_columns:list)->pd.DataFrame:
    try:
        columns=[column for column in df.columns if column not in exclude_columns]
        for column in columns:
            if df[column].dtype!='O':
                df[column]=df[column].astype(np.float64)
        
        return df

    except Exception as e:
        raise InsuranceException(e,sys)
    

def write_yaml_file(file_path,data:dict):
    try:
        file_dir=os.path.dirname(file_path)
        os.makedirs(file_dir,exist_ok=True)
        with open(file_path,'w') as file:
            yaml.dump(data,file)

    except Exception as e:
        raise InsuranceException(e,sys)
    

def save_object(file_path:str,obj:object)->None:
    try:
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path,'wb') as file_obj:
            dill.dump(obj,file_obj)


    except Exception as e:
        raise InsuranceException(e,sys)
    

def load_object(file_path:str,)->object:
    try:
        if not os.path.exists(file_path):
            raise Exception(f'The file:{file_path} is not available')
        else:
            with open(file_path,'rb') as file_obj:
                return dill.open(file_obj)
         
    except Exception as e:
        raise InsuranceException(e,sys)

