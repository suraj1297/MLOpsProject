import os
import sys
from src.components import data_ingestion, data_transformation, model_trainer
from src.exception import CustomException
from src.logger import logging


class GetBestModel():

    def __init__(self) -> None:
        self.di = data_ingestion.DataIngestion()
        self.dt = data_transformation.DataTransformation()
        self.train_model = model_trainer.ModelTrainer()
        self.train_path = self.di.data_config.train_data_path
        self.test_path = self.di.data_config.test_data_path

    def start_pipeline(self):

        try:

            logging.info("Starting Data Ingestion")

            self.di.initiate_data_ingestion()

            logging.info("Starting Data Transformation")

            train_data, test_data, preprocessor_file_path = self.dt.initiate_data_transformation(self.train_path, self.test_path)

            logging.info('Starting training Models')

            self.train_model.initiate_model_training(train_data, test_data, preprocessor_file_path)

            logging.info(f'Saved Best Model at path: {self.train_model.trainer_config.trained_model_path}')

            logging.info("Pipeline Executed")

        except Exception as e:
            logging.debug(e)
            raise CustomException(e, sys) from None
        

if __name__ == "__main__":
    GetBestModel().start_pipeline()