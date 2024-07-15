from Insurance.logger import logging
from Insurance.exception import InsuranceException
import os,sys
from Insurance.utils import get_collection_as_dataframe
from Insurance.entity.config_entity import TrainingpipelineConfig,DataIngestionConfig
from Insurance.components.data_ingestion import DataIngestion

if __name__=="__main__":
    try:
        #get_collection_as_dataframe()
        training_pipeline_config=TrainingpipelineConfig()

        data_ingestion_config=DataIngestionConfig(training_pipeline_config)
        print(data_ingestion_config.data_to_dict())

        logging.info('initiating the steps of data ingestion.')
        data_ingestion=DataIngestion(data_ingesttion_config=data_ingestion_config)
        data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
        #This will spit out the paths of feature store,train file path,test file path

    except Exception as e:
        logging.info(e)
        raise InsuranceException(e,sys)