import os
import sys
import numpy as np
import pandas as pd
import dill
from src.exception import CustomException
from src.logger import logging
from sklearn.metrics import r2_score

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

            ml.fit(X_train, y_train)

            train_r2 = r2_score(y_train, ml.predict(X_train) )
            test_r2 = r2_score(y_test, ml.predict(X_test) )


            scores[model] = [ml, test_r2]

        
        return scores


    except Exception as e:
        logging.debug(e)
        raise CustomException(e, sys) from None