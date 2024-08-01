import os,sys
from datetime import datetime
from Insurance.exception import InsuranceException
from Insurance.logger import logging

FILE_NAME="insurance.csv"
TRAIN_FILE_NAME="train.csv"
TEST_FILE_NAME="test.csv"
TRANSFORMER_OBJECT_FILE_NAME='transformer.pkl'
TRANSFORMED_TRAIN_FILE_NAME='tramsformed_train.csv'
TRANSFORMED_TEST_FILE_NAME='transformed_test.csv'
TRANSFORMER_TARGET_ENCODER_FILE_PATH='target_encoder.pkl'


class TrainingpipelineConfig:
    def __init__(self):
        try:
            self.artifact_dir=os.path.join(os.getcwd(),'artifact',f"{datetime.now().strftime("%m%d%Y-%H%M%S")}")
        except Exception as e:
            raise InsuranceException(e,sys)

class DataIngestionConfig:
    def __init__(self,training_pipeline_config:TrainingpipelineConfig):
        try:
            self.database_name="INSURANCE" 
            self.collection_name="INSURANCE_PROJECT"
            self.data_ingestion_dir=os.path.join(training_pipeline_config.artifact_dir,"data_ingestion")
            self.feature_store_file_path=os.path.join(self.data_ingestion_dir,"feature_store",FILE_NAME)
            self.train_file_path=os.path.join(self.data_ingestion_dir,"dataset",TRAIN_FILE_NAME)
            self.test_file_path=os.path.join(self.data_ingestion_dir,"dataset",TEST_FILE_NAME)
            self.test_size=0.2
        except Exception as e:
            raise InsuranceException(e,sys)
        
    #Convert data to dict

    def data_to_dict(self,)->dict:
        try:
            return self.__dict__
        except Exception as e:
            raise InsuranceException(e,sys)
        
class DataValidationConfig:

    def __init__(self,training_pipeline_config:TrainingpipelineConfig):
        try:
            self.data_validation_dir:str=os.path.join(training_pipeline_config.artifact_dir,'data_validation')
            self.report_file_path=os.path.join(self.data_validation_dir,
                                               'reprot.yaml') #Report can be of yaml or json or some other formats also.
            self.MISSING_THRESHOLD=0.2
            self.base_file_path=os.path.join('insurance.csv')
            
        except Exception as e:
            raise InsuranceException(e,sys)
        
class DataTransformationConfig:

    def __init__(self,training_pipeline_config:TrainingpipelineConfig):
        try:
            self.data_transformation_dir:str=os.path.join(training_pipeline_config.artifact_dir,'data_transformation')
            self.transformer_object_path:str=os.path.join(self.data_transformation_dir,TRANSFORMER_OBJECT_FILE_NAME)
            self.transformed_train_path:str=os.path.join(self.data_transformation_dir,TRAIN_FILE_NAME.replace("csv","npz"))
            self.transformed_test_path:str=os.path.join(self.data_transformation_dir,TEST_FILE_NAME.replace("csv","npz"))
            self.target_encoder_path:str=os.path.join(self.data_transformation_dir,TRANSFORMER_TARGET_ENCODER_FILE_PATH)


        except Exception as e:
            raise InsuranceException(e,sys)

        


