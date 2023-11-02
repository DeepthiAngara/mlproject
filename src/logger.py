import logging
import os
import datetime

cdt = datetime.datetime.now().strftime('%m_%d_%Y_%H_%M_%S')
LOG_FILE = cdt + '.log'
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)

try:
    os.makedirs(logs_path)
except FileExistsError:
    LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)
    pass


logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)




