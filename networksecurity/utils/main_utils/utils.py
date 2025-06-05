import yaml
import os
import sys
import numpy as np
import dill
import pickle
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

def read_yaml_file(file_path: str) -> dict:
    try:
        with open(file_path, 'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise NetworkSecurityException(e, sys) from e

def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    try:
        # Ensure the directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # If file exists and replace is False, skip writing
        if not replace and os.path.exists(file_path):
            logging.info(f"File '{file_path}' already exists and replace=False, skipping write.")
            return

        # Write the content to the YAML file
        with open(file_path, "w") as file:
            yaml.dump(content, file)

    except Exception as e:
        raise NetworkSecurityException(e, sys) from e

def save_numpy_array_data(file_path: str, array: np.ndarray) -> None:
    """
    Save a NumPy array to a .npy file.

    Args:
        file_path (str): Path to save the NumPy array.
        array (np.ndarray): The NumPy array to save.
    """
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            np.save(file_obj, array)
        logging.info(f"NumPy array saved successfully to: {file_path}")
    except Exception as e:
        raise NetworkSecurityException(e, sys) from e
def save_object(file_path: str, obj: object) -> None:

    try:
        logging.info("entered save_object")
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
        logging.info(f"Object saved successfully to: {file_path}")
    except Exception as e:
        raise NetworkSecurityException(e, sys) from e
