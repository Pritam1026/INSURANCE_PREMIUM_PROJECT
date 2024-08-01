from Insurance.logger import logging
from Insurance.exception import InsuranceException
import os,sys
from Insurance.utils import get_collection_as_dataframe
from Insurance.entity.config_entity import TrainingpipelineConfig,DataIngestionConfig,DataValidationConfig,DataTransformationConfig
from Insurance.components.data_ingestion import DataIngestion
from Insurance.components.data_validation import DataValidation
from Insurance.components.data_transformatiom import DataTransFormation


if __name__=="__main__":
    try:
        #get_collection_as_dataframe()
        training_pipeline_config=TrainingpipelineConfig()

        data_ingestion_config=DataIngestionConfig(training_pipeline_config)
        print(data_ingestion_config.data_to_dict())


        #Data Ingestion
        logging.info('initiating the steps of data ingestion.')
        data_ingestion=DataIngestion(data_ingesttion_config=data_ingestion_config)
        data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
        #This will spit out the paths of feature store,train file path,test file path

        #Data Validation
        logging.info('Initiating the steps of data validation')
        data_validation_config=DataValidationConfig(training_pipeline_config=training_pipeline_config)
        data_validation=DataValidation(data_validation_config=data_validation_config,
                                       data_ingestion_artifact=data_ingestion_artifact)
        data_validation_artifact=data_validation.initiate_data_validation()

        #Data Transformation
        data_transformation_config=DataTransformationConfig(training_pipeline_config=training_pipeline_config)
        data_transformmation=DataTransFormation(data_transformation_config=data_transformation_config,
                                                data_ingestion_artifact=data_ingestion_artifact)
        data_tranformation_artifact=data_transformmation.initiate_data_transformation()

    except Exception as e:
        logging.info(e)
        raise InsuranceException(e,sys)