import pandas as pd
import numpy as np

from Insurance.entity import artifact_entity,config_entity
from Insurance.logger import logging
from Insurance.exception import InsuranceException
from Insurance.config import TARGET_COLUMN
from Insurance.utils import convert_columns_float
from Insurance import utils
from typing import Optional

import os,sys

from scipy.stats import ks_2samp





class DataValidation:
    def __init__(self,data_validation_config:config_entity.DataValidationConfig,
                 data_ingestion_artifact:artifact_entity.DataIngestionArtifact):
        try:

            logging.info("**********************DATA VALIDATION********************************************")
            self.data_validation_config=data_validation_config
            self.data_ingestion_artifact=data_ingestion_artifact
            self.validation_error=dict()
        except Exception as e:
            raise InsuranceException(e,sys)


    def drop_missing_values_columns(self,df:pd.DataFrame,report_key_name:str)->Optional[pd.DataFrame]:
        try:
            thrshold=self.data_validation_config.MISSING_THRESHOLD
            null_report=df.isnull().sum()/df.shape[0]
            drop_column_names=null_report[null_report>thrshold].index
            self.validation_error[report_key_name]=list(drop_column_names)
            df.drop(list(drop_column_names),axis=1,inplace=True)

            if len(df.columns)==0:
                return None
            else:
                return df


        except Exception as e:
            raise InsuranceException(e,sys)

    def is_required_column_exists(self,base_df:pd.DataFrame,current_df:pd.DataFrame,report_key_name:str)->bool:
        try:
            base_columns=base_df.columns
            current_columns=current_df.columns

            missing_columns=[]
            for base_column in base_columns:
                if base_column not in current_columns:
                    missing_columns.append(base_column)

            if len(missing_columns)>0:
                self.validation_error[report_key_name]=missing_columns
                return False
            else:
                return True



        except Exception as e:
            raise InsuranceException(e,sys)

    def data_drift(self,base_df:pd.DataFrame,current_df:pd.DataFrame,report_key_name:str):
        try:
            drift_report=dict()
            base_columns=base_df.columns
            current_columns=current_df.columns

            for base_column,current_column in zip(base_columns,current_columns):
                same_distribution=ks_2samp(base_df[base_column],current_df[current_column])

                

                if same_distribution[1]>0.05:
                    drift_report[base_column]={'P-value':float(same_distribution[1]),
                                               'same_distribution':True
                                               }
                else:
                    drift_report[base_column]={'P-value':float(same_distribution[1]),
                                               'same_distribution':False
                                               }
            
            self.validation_error[report_key_name]=drift_report

        except Exception as e:
            raise InsuranceException(e,sys)
    

    def initiate_data_validation(self)->artifact_entity.DataIngestionArtifact:
        try:
            base_df=pd.read_csv(self.data_validation_config.base_file_path)
            base_df.replace(to_replace='na',value=np.NaN,inplace=True)
            base_df=self.drop_missing_values_columns(base_df,report_key_name='Missing_value_within_base_data')
            
            train_df=pd.read_csv(self.data_ingestion_artifact.train_file_path)
            test_df=pd.read_csv(self.data_ingestion_artifact.test_file_path)

            train_df=self.drop_missing_values_columns(df=train_df,
                                                      report_key_name="Missing Value within Base dataset")
            test_df=self.drop_missing_values_columns(df=test_df,
                                                     report_key_name='Missing value within base dataset')
            
            exclude_column=[TARGET_COLUMN]
            base_df=convert_columns_float(df=base_df,exclude_columns=exclude_column)
            train_df=convert_columns_float(df=train_df,exclude_columns=exclude_column)
            test_df=convert_columns_float(df=test_df,exclude_columns=exclude_column)

            train_df_column_status=self.is_required_column_exists(base_df=base_df,current_df=train_df,
                                                                  report_key_name='missing_column_within_train_dataset')
            
            test_df_column_status=self.is_required_column_exists(base_df=base_df,current_df=test_df,
                                                                  report_key_name='missing_column_within_test_dataset')
            
            if train_df_column_status:
                self.data_drift(base_df=base_df,current_df=train_df,
                                report_key_name="data_drift_within_train_dataset")
                
            if test_df_column_status:
                self.data_drift(base_df=base_df,current_df=test_df,
                                report_key_name="data_drift_within_test_dataset")

            #Write your 
            utils.write_yaml_file(file_path=self.data_validation_config.report_file_path,
                            data=self.validation_error)
            
            data_validation_artifact= artifact_entity.DataValidationArtifact(report_file_path=self.data_validation_config.report_file_path)
        

                
            return data_validation_artifact
   
        except Exception as e:
            raise InsuranceException(e,sys)

