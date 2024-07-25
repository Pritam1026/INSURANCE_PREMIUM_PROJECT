import pandas as pd
import numpy as np
import os
import sys
from Insurance.entity import config_entity,artifact_entity
from Insurance.exception import InsuranceException
from Insurance.utils import get_collection_as_dataframe
from Insurance.logger import logging
from sklearn.model_selection import train_test_split

class DataIngestion:
    def __init__(self,data_ingesttion_config:config_entity.DataIngestionConfig):
        try:
            self.data_ingestion_config=data_ingesttion_config
        except Exception as e:
            raise InsuranceException(e,sys)
        
    def initiate_data_ingestion(self,)->artifact_entity.DataIngestionArtifact:
        try:
            logging.info("Exporting collection as pandas dataframe")
            df:pd.DataFrame=get_collection_as_dataframe(
                database_name=self.data_ingestion_config.database_name,
                collection_name=self.data_ingestion_config.collection_name)
            
            #Replacing na with NAN
            df.replace(to_replace='na',value=np.NaN,inplace=True)

            #Saving data into feature store
            logging.info("Creating a feature store folder if not available")
            feature_store_dir=os.path.dirname(self.data_ingestion_config.feature_store_file_path)
            os.makedirs(feature_store_dir,exist_ok=True)

            logging.info("Saving the data to feature store.")
            df.to_csv(path_or_buf=self.data_ingestion_config.feature_store_file_path,index=False,header=True)

            #Splitting the data into train and test set.
            logging.info("Splitting the data into train and test set")
            train_df:pd.DataFrame=pd.DataFrame()
            test_df:pd.DataFrame=pd.DataFrame()
            train_df,test_df=train_test_split(df,test_size=self.data_ingestion_config.test_size,random_state=1)

            dataset_dir=os.path.dirname(self.data_ingestion_config.train_file_path) 
            #Any of the train or test file path can be used to get the path
            os.makedirs(dataset_dir,exist_ok=True)

            #Saving the train and test files
            train_df.to_csv(path_or_buf=self.data_ingestion_config.train_file_path,index=False,header=True)
            test_df.to_csv(path_or_buf=self.data_ingestion_config.test_file_path,index=False,header=True)

            #prepare the artifact foldr
            data_ingestion_artifact=artifact_entity.DataIngestionArtifact(
                feature_store_file_path=self.data_ingestion_config.feature_store_file_path,
                train_file_path=self.data_ingestion_config.train_file_path,
                test_file_path=self.data_ingestion_config.test_file_path
            )

            return data_ingestion_artifact

        except Exception as e:
            raise InsuranceException(e,sys)
        
        


