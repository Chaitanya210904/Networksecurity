import os
import sys
import numpy as np
import pandas as pd


TARGET_COLUMN="Result"
PIPELINE_NAME: str="NetworkSecurity"
ARTIFACT_DIR: str="Artifact"
FILE_NAME: str ="phisingData.csv"
TEST_FILE_NAME: str="test.csv"
TRAIN_FILE_NAME: str="train.csv"


DATA_INGESTION_COLLECTION_NAME: str="NetworkData"
DATA_INGESTION_DATABASE_NAME: str="chaitanyaproj"
DATA_INGESTION_DIR_NAME: str="data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str="feature_store"
DATA_INGESTION_INGESTED_DIR: str="ingested"
DATA_INGESTION_TEST_TRAIN_SPLIT_RATIO: float=0.2