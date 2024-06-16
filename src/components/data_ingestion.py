import os
import sys
from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass
import pandas as pd
from sklearn.model_selection import train_test_split
from src.components.data_transformation import DataTransformation

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str= os.path.join('artifacts', "test.csv")
    raw_data_path: str= os.path.join('artifacts', 'raw.csv')


class DataIngestion:

    def __init__(self) -> None:
        self.data_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            data = pd.read_csv("notebook/data/stud.csv")
            logging.info("Reading data csv file")

            os.makedirs(os.path.dirname(self.data_config.train_data_path), exist_ok=True)

            data.to_csv(self.data_config.raw_data_path, index=False)

            train_set, test_set = train_test_split(data, test_size=0.2, random_state=0)

            train_set.to_csv(self.data_config.train_data_path, index=False)
            test_set.to_csv(self.data_config.test_data_path, index=False)

            logging.info("Created data artifacts")

        except Exception as e:
            logging.debug(e)
            raise CustomException(e, sys) from None
        

if __name__ == "__main__":
   di =  DataIngestion()
   di.initiate_data_ingestion()

   dt = DataTransformation()
   dt.initiate_data_transformation(di.data_config.train_data_path, di.data_config.test_data_path)


