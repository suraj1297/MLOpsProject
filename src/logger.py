import logging
import os


logging.basicConfig(
    filename= os.path.join(os.getcwd(), 'logs.log'),
    format='%(asctime)s : %(levelname)s : %(name)s :  %(filename)s : %(lineno)d: %(message)s',
    level=10
)


if __name__ == "__main__":
    logging.info("Logging has Started")