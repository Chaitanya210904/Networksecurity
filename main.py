from networksecurity.components.data_injestion import DataIngestion
from networksecurity.components.data_validataion import DataValidation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig, DataTransformationConfig
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.entity.config_entity import ModelTrainerConfig
from networksecurity.components.model_trainer import ModelTrainer



import sys

if __name__ == '__main__':
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        
        
        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
        dataingestion = DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        dataingestionartifact = dataingestion.initiate_data_ingestion()
        logging.info("Data ingestion completed")
        print(dataingestionartifact)
        
        
        data_validation_config = DataValidationConfig(trainingpipelineconfig)
        data_validation = DataValidation(dataingestionartifact, data_validation_config)  # ✅ FIXED HERE
        logging.info("Initiate the data validation")
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info("Data validation completed")
        print(data_validation_artifact)
        data_transformation_config=DataTransformationConfig(trainingpipelineconfig)
        logging.info("Data transformation started")
        data_transformation=DataTransformation(data_validation_artifact,data_transformation_config)
        data_transformation_artifact=data_transformation.initiate_data_transformation()
        print(data_transformation_artifact)
        logging.info("Data transformation completed")
        logging.info("Model Training started")
        model_trainer_config=ModelTrainerConfig(trainingpipelineconfig)
        model_trainer=ModelTrainer(model_trainer_config=model_trainer_config,data_transformation_artifact=data_transformation_artifact)
        model_trainer_artifact=model_trainer.initiate_model_trainer()
        logging.info("Model training artifact created")

    except Exception as e:
        raise NetworkSecurityException(e, sys)
