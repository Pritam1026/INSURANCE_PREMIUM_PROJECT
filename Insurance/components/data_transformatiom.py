import pandas as pd




from Insurance.entity import config_entity,artifact_entity
from sklearn.pipeline import Pipeline
from Insurance.exception import InsuranceException
import os,sys
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import RobustScaler,LabelEncoder
from Insurance.config import TARGET_COLUMN
from Insurance.utils import save_object



# Missing value impute
# Outlier handling
# Imbalance data handling
# Convert categorical data into numerical data






class DataTransFormation:
    def __init__(self,data_transformation_config:config_entity.DataTransformationConfig,
                 data_ingestion_artifact:artifact_entity.DataIngestionArtifact):
        try:
            self.data_transformation_config=data_transformation_config
            self.data_ingestion_artifact=data_ingestion_artifact
        except Exception as e:
            raise InsuranceException(e,sys)

    @classmethod
    def get_data_transformer_object(cls)->Pipeline:
        try:
            simple_imputer=SimpleImputer(strategy='mean')
            robust_scaler=RobustScaler()
            pipeline=Pipeline(steps=[('imputer',simple_imputer),
                                     ('robust_scalerr',robust_scaler)])
            return pipeline
        
        except Exception as e:
            raise InsuranceException(e,sys)

    def initiate_data_transformation(self,)->artifact_entity.DataValidationArtifact:
        try:
            train_df=pd.read_csv(self.data_ingestion_artifact.train_file_path)
            test_df=pd.read_csv(self.data_ingestion_artifact.test_file_path)

            input_feature_train_df=train_df.drop(TARGET_COLUMN,axis=1)
            input_feature_test_df=test_df.drop(TARGET_COLUMN,axis=1)

            target_feature_train_df=train_df[TARGET_COLUMN]
            target_feature_test_df=test_df[TARGET_COLUMN]

            label_encoder=LabelEncoder()

            target_feature_train_arr=target_feature_train_df.squeeze()
            target_feature_test_arr=target_feature_test_df.squeeze()

            for col in input_feature_train_df.columns:
                if input_feature_train_df[col].dtype=='O':
                    input_feature_train_df[col]=label_encoder.fit_transform(input_feature_train_df[col])
                    input_feature_test_df[col]=label_encoder.transform(input_feature_test_df[col])
                

            transformation_pipeline=DataTransFormation.get_data_transformer_object()
            transformation_pipeline.fit(input_feature_train_df)

            input_feature_train_arr=transformation_pipeline.transform(input_feature_train_df)
            input_feature_test_arr=transformation_pipeline.transform(input_feature_test_df)

            save_object(file_path=self.data_transformation_config.transformer_object_path,
                              obj=transformation_pipeline)
            save_object(file_path=self.data_transformation_config.target_encoder_path,obj=label_encoder)

            data_transformation_artifact=artifact_entity.DataTransformationArtifact(
            transformer_object_path=self.data_transformation_config.transformer_object_path,
            transformed_train_path=self.data_transformation_config.transformed_train_path,
            transformed_test_path=self.data_transformation_config.transformed_test_path
            )

            return data_transformation_artifact

        except Exception as e:
            raise InsuranceException(e,sys)




    



