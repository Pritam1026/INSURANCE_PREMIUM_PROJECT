from typing import Optional
import os,sys
from Insurance.exception import InsuranceException
from Insurance.entity.config_entity import TRANSFORMER_OBJECT_FILE_NAME,MODEL_FILE_NAME,TRANSFORMER_TARGET_ENCODER_FILE_PATH


class ModelResolver:

    def __init__(self,model_registry:str="saved_models",
                 transformer_dir_name:str="transformer",
                 targer_encoder_dir_name:str="target_encoder",
                 model_dir_name:str="model"):
        self.model_registry=model_registry
        os.makedirs(self.model_registry,exist_ok=True)
        self.transformer_dir_name=transformer_dir_name
        self.targer_encoder_dir_name=targer_encoder_dir_name
        self.model_dir_name=model_dir_name

    def get_latest_dir_path(self,)->Optional[str]:

        try:
            dir_name=os.listdir(self.model_registry)
            if len(dir_name)==0:
                return None
            dir_name=list(map(int,dir_name))
            latest_dir_name=max(dir_name)
            return os.path.join(self.model_registry,f"{latest_dir_name}")
        
        except Exception as e:
            raise InsuranceException(e,sys)
        
    def get_latest_model_path(self,):
        try:
            latest_dir=self.get_latest_dir_path()
            if latest_dir is None:
                raise Exception("Model is not available")
            return os.path.join(latest_dir,self.model_dir_name,MODEL_FILE_NAME)
            
        except Exception as e:
            raise InsuranceException(e,sys)

    def get_latest_transformer_path(self,):
        try:
            latest_dir=self.get_latest_dir_path()
            if latest_dir is None:
                raise Exception("Transformer object is not available")
            return os.path.join(latest_dir,self.transformer_dir_name,TRANSFORMER_OBJECT_FILE_NAME)
        except Exception as e:
            raise InsuranceException(e,sys)

    def get_latest_target_encoder_path(self,):
        try:
            latest_dir=self.get_latest_dir_path()
            if latest_dir is None:
                raise Exception("Target encoder object is not available")
            return os.path.join(latest_dir,self.targer_encoder_dir_name,TRANSFORMER_TARGET_ENCODER_FILE_PATH)
        except Exception as e:
            raise InsuranceException(e,sys)
        

    def get_latest_save_dir_path(self,)->str:
        try:
            latest_dir=self.get_latest_dir_path()
            if latest_dir is None:
                return os.path.join(self.model_registry,f'{0}')
            latest_dir_num=int(os.path.basename(self.get_latest_dir_path()))
            return os.path.join(self.model_registry,f"{latest_dir_num}")
        except Exception as e:
            raise InsuranceException(e,sys)
        

    def get_latest_save_model_path(self,):
        try:
            latest_dir=self.get_latest_save_dir_path()
            return os.path.join(latest_dir,self.model_dir_name,MODEL_FILE_NAME)
        except Exception as e:
            raise InsuranceException(e,sys)
        
    
    def get_latest_save_transformer_path(self,):
        try:
            latest_dir=self.get_latest_save_dir_path()
            return os.path.join(latest_dir,self.transformer_dir_name,TRANSFORMER_OBJECT_FILE_NAME)
        except Exception as e:
            raise InsuranceException(e,sys)


    def get_latest_save_target_encoder_path(self,):
        try:
            latest_dir=self.get_latest_save_dir_path()
            return os.path.join(latest_dir,self.targer_encoder_dir_name,TRANSFORMER_TARGET_ENCODER_FILE_PATH)
        except Exception as e:
            raise InsuranceException(e,sys)



    
