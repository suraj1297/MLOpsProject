import logging
import os
import datetime
import time

log_filename = f'{str(datetime.date.fromtimestamp(time.time()))}'
log_file_path = os.path.join(f'{os.getcwd()}', "logs", log_filename)

os.makedirs(log_file_path, exist_ok=True)



logging.basicConfig(
    filename= os.path.join(log_file_path, 'logs.log'),
    format='%(asctime)s : %(levelname)s : %(name)s :  %(filename)s : %(lineno)d: %(message)s',
    level=10
)


if __name__ == "__main__":
    logging.info("Logging has Started")