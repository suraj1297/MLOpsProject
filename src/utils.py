import os
import sys
import numpy as np
import pandas as pd
import dill
from src.exception import CustomException
from src.logger import logging
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
from src.components.params import params
import pickle

def save_object(file_path, object):

    try:

        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as fileobj:
            dill.dump(object, fileobj)

    except Exception as e:
        logging.debug(e)
        raise CustomException(e, sys) from None


def evaluate_models(X_train, y_train, X_test, y_test, models):
    try:
        scores = {}

        for model in models.keys():

            logging.info(f"Training model: {model}")

            ml = models[model]
            logging.info(ml)

            if model=="LR":
                ml.fit(X_train, y_train)
                train_r2 = r2_score(y_train, ml.predict(X_train) )
                test_r2 = r2_score(y_test, ml.predict(X_test) )
                scores[model] = [ml, test_r2]
            else:
                gsc = GridSearchCV( ml, params(model), n_jobs=-1, cv=5, scoring="r2")

                logging.info(gsc)
                gsc.fit(X_train, y_train)

                train_r2 = r2_score(y_train, gsc.predict(X_train) )
                test_r2 = r2_score(y_test, gsc.predict(X_test) )

                scores[model] = [gsc, test_r2]
        
        return scores


    except Exception as e:
        logging.debug(e)
        raise CustomException(e, sys) from None
    
def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)