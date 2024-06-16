import os
import sys
import numpy as np
import pandas as pd
import dill
from src.exception import CustomException
from src.logger import logging


def save_object(file_path, object):

    try:

        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as fileobj:
            dill.dump(object, fileobj)

    except Exception as e:
        logging.debug(e)
        raise CustomException(e, sys) from None
