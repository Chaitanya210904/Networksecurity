import os
import sys
import numpy as np
import pandas as pd

TARGET_COLUMN = "Result"
PIPELINE_NAME: str = "NetworkSecurity"
ARTIFACT_DIR: str = "Artifact"
FILE_NAME: str = "phisingData.csv"
TEST_FILE_NAME: str = "test.csv"
TRAIN_FILE_NAME: str = "train.csv"
SCHEMA_FILE_PATH = os.path.join("data_schema", "schema.yaml")
SAVED_MODEL_DIR=os.path.join("saved_models")
MODEL_FILE_NAME = "model.pkl"

DATA_INGESTION_COLLECTION_NAME: str = "NetworkData"
DATA_INGESTION_DATABASE_NAME: str = "chaitanyaproj"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TEST_TRAIN_SPLIT_RATIO: float = 0.2

DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_VALID_DIR: str = "validated"
DATA_VALIDATION_INVALID_DIR: str = "invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR: str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME: str = "report.yaml"

DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DIR: str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR: str = "transformed_object"
DATA_TRANSFORMATION_IMPUTER_PARAMS: dict = {
    "missing_values": np.nan,
    "n_neighbors": 3,
    "weights": "uniform",
}
TRANSFORMED_TRAIN_FILE_NAME = "train.npy"
TRANSFORMED_TEST_FILE_NAME = "test.npy"
PREPROCESSOR_OBJECT_FILE_NAME = "preprocessor.pkl"

MODEL_TRAINER_DIR_NAME: str="model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR: str = "trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME: str = "model.pkl"
MODEL_TRAINER_OVER_FITTING_OVER_FITTING_UNDER_FITTING_THRESHOLD: float =0.05
MODEL_TRAINER_EXPECTED_SCORE: float=0.6

