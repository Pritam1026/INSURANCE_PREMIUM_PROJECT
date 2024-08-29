from Insurance.logger import logging
from Insurance.exception import InsuranceException
import os,sys
from Insurance.utils import get_collection_as_dataframe
from Insurance.entity.config_entity import TrainingpipelineConfig,DataIngestionConfig,DataValidationConfig,DataTransformationConfig,ModelTrainingConfig,ModelEvaluationConfig
from Insurance.components.data_ingestion import DataIngestion
from Insurance.components.data_validation import DataValidation
from Insurance.components.data_transformatiom import DataTransFormation
from Insurance.components.model_trainer import ModelTrainer
from Insurance.components.model_evaluation import ModelEvaluation 


if __name__=="__main__":
    try:
        #get_collection_as_dataframe()
        training_pipeline_config=TrainingpipelineConfig()

        data_ingestion_config=DataIngestionConfig(training_pipeline_config)
        print(data_ingestion_config.data_to_dict())


        #----------------Data Ingestion---------------------------------------------------------
        logging.info('---------------Initiating the steps of data ingestion.---------------------------------')
        data_ingestion=DataIngestion(data_ingesttion_config=data_ingestion_config)
        data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
        #This will spit out the paths of feature store,train file path,test file path
        logging.info('---------------data ingestion done--------------------------')



        #----------------Data Validation--------------------------------------------------------
        logging.info('---------------Initiating the steps of data validation---------------------------------')
        data_validation_config=DataValidationConfig(training_pipeline_config=training_pipeline_config)
        data_validation=DataValidation(data_validation_config=data_validation_config,
                                       data_ingestion_artifact=data_ingestion_artifact)
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info('---------------data validation done--------------------------')



        #----------------Data Transformation-----------------------------------------------------
        logging.info('---------------Initiating the steps of data transformation------------------------------')
        data_transformation_config=DataTransformationConfig(training_pipeline_config=training_pipeline_config)
        data_transformmation=DataTransFormation(data_transformation_config=data_transformation_config,
                                                data_ingestion_artifact=data_ingestion_artifact)
        data_tranformation_artifact=data_transformmation.initiate_data_transformation()
        logging.info('---------------data transformation done--------------------------')



        #----------------Model Trainer-------------------------------------------------------------
        logging.info('---------------Initiating the steps of model training------------------------------')
        model_trainer_config=ModelTrainingConfig(training_pipeline_config=training_pipeline_config)
        model_trainer=ModelTrainer(model_trainer_config=model_trainer_config,
                                   data_transformation_artifact=data_tranformation_artifact)
        model_trainer_artifact=model_trainer.initiate_model_trainer()
        logging.info('---------------Model training and model saving done--------------------------')



        #-----------------Model Evaluation----------------------------------------------------------
        logging.info('-----------------Initiating the steps of model evaluation---------------------------')
        model_eval_config=ModelEvaluationConfig(training_pipeline_config=training_pipeline_config)
        model_eval=ModelEvaluation(model_eval_config=model_eval_config,
                                   data_ingestion_artifact=data_ingestion_artifact,
                                   data_transformation_artifact=data_tranformation_artifact,
                                   model_trainer_artifact=model_trainer_artifact)
        
        model_eval_artifact=model_eval.initiate_model_evaluation()


    except Exception as e:
        logging.info(e)
        raise InsuranceException(e,sys)