import os
import sys
from dataclasses import dataclass

from sklearn.ensemble import AdaBoostRegressor, GradientBoostingRegressor, RandomForestRegressor

from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from xgboost import XGBRegressor

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object, evaluate_models


@dataclass
class ModelTrainerConfig:
    trained_model_path = os.path.join("artifacts", "pickles" ,"model.pkl")


class ModelTrainer:

    def __init__(self) -> None:
        self.trainer_config = ModelTrainerConfig()

    def initiate_model_training(self, train_array, test_array, preprocessor_path):
        try:
            logging.info("Reading data fro model training")

            X_train = train_array[:, :-1]
            y_train = train_array[:, -1]
            X_test = test_array[:, :-1]
            y_test = test_array[:, -1]

            logging.info("Read Data Successfully")

            models = {
                "LR": LinearRegression(),
                "SVR": SVR(),
                "KNN": KNeighborsRegressor(),
                "DT": DecisionTreeRegressor(max_depth=5),
                "XGB": XGBRegressor(),
                "ADB": AdaBoostRegressor(),
                "GBR": GradientBoostingRegressor(),
                "RF": RandomForestRegressor()
            }
            logging.info("Evaluating Models")

            model_scores = evaluate_models(X_train, y_train, X_test, y_test, models)

            logging.info("Evaluated Models")

            max_score = -1000
            best_model = []

            logging.info("Fetching best Model")

            for model_name in model_scores.keys():
                if model_scores[model_name][1] > max_score:
                    max_score = model_scores[model_name][1]
                    best_model = [ model_name, model_scores[model_name][0]]
                logging.info(f"Model Score: {model_name}, score: { model_scores[model_name][1]}")

            logging.info("Saving best Models")
            print(best_model)

            save_object(self.trainer_config.trained_model_path, best_model[1])

            logging.info("Saved Best")

        except Exception as e:
            logging.debug(e)
            raise CustomException(e, sys) from None