from Insurance.logger import logging
from Insurance.exception import InsuranceException
import os,sys
from Insurance.utils import get_collection_as_dataframe
from Insurance.entity.config_entity import TrainingpipelineConfig,DataIngestionConfig

if __name__=="__main__":
    try:
        #get_collection_as_dataframe()
        training_pipeline_config=TrainingpipelineConfig()
        data_ingestion_config=DataIngestionConfig(training_pipeline_config)
        print(data_ingestion_config.data_to_dict())
    except Exception as e:
        logging.info(e)
        raise InsuranceException(e,sys)