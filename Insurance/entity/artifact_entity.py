from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    feature_store_file_path:str
    train_file_path:str
    test_file_path:str

@dataclass
class DataValidationArtifact:
    report_file_path:str

@dataclass
class DataTransformationArtifact:
    transformer_object_path:str
    transformed_train_path:str
    transformed_test_path:str


@dataclass
class ModelTrainerArtifact:
    model_path:str
    r2_train_score:int
    r2_test_score:int

@dataclass
class ModelEvaluationArtifact:
    is_model_accepted:bool
    improved_accuracy:float