import os
import sys
from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
import numpy as np
import pandas as pd
from src.utils import save_object


@dataclass
class DataTransformationConfig:
    preprocessor_file_path = os.path.join("artifacts", 'pickles' ,'prepocessor.pkl')


class DataTransformation:

    def __init__(self) -> None:
        self.data_tran_config = DataTransformationConfig()

    def get_data_transformation_object(self):

        try:
            numerical_features = ['reading_score', 'writing_score']
            categorical_features = ['gender', 'race_ethnicity', 'parental_level_of_education', 'lunch','test_preparation_course']


            num_pipeline = Pipeline(
                [('imputer', SimpleImputer(strategy="median")),
                ('scaler', StandardScaler())]
            )

            logging.info("Created Numerical Pipeline")

            cat_pipeline = Pipeline(
                [('imputer', SimpleImputer(strategy="most_frequent")),
                ('one', OneHotEncoder()),
                ('scaler', StandardScaler(with_mean=False))]
            )

            logging.info('Create Categorical pipeline')
            
            preprocessor = ColumnTransformer(
                [
                    ("num_pipeline", num_pipeline, numerical_features),
                    ("cat_pipeline", cat_pipeline, categorical_features)
                ]
            )
            logging.info("Created ColumnTransformer")

            return preprocessor

        except Exception as e:
            logging.debug(e)
            CustomException(e, sys)

    def initiate_data_transformation(self, train_path, test_path):
        try:
            
            train_data = pd.read_csv(train_path)
            test_data = pd.read_csv(test_path)

            logging.info("Read data for Transformation")

            preprocessing_object = self.get_data_transformation_object()

            logging.info("Created Data Transformation Object")

            input_train_data = train_data.drop(columns=["math_score"], axis = 1)
            input_train_y = train_data["math_score"]

            input_test_data = test_data.drop(columns=["math_score"], axis=1)
            input_test_y = test_data["math_score"]

            logging.info("Dropped Target feature from train n test data")

            input_feature_train_data = preprocessing_object.fit_transform(input_train_data)
            input_features_test_data = preprocessing_object.transform(input_test_data)


            transformed_train = np.c_[input_feature_train_data, input_train_y]
            transformed_test = np.c_[input_features_test_data, input_test_y]

            save_object( self.data_tran_config.preprocessor_file_path, preprocessing_object)

            
            return transformed_train, transformed_test, self.data_tran_config.preprocessor_file_path


        except Exception as e:
            logging.debug(e)
            raise CustomException(e, sys) from None




if __name__ == "__main__":
    DataTransformation().initiate_data_transformation()