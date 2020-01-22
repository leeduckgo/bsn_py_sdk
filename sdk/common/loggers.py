import logging
from logging.handlers import TimedRotatingFileHandler, RotatingFileHandler

# init logging
logging.basicConfig()

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)

# the path of logger
logs_path = ".\\logs\\"


fh = RotatingFileHandler(filename=logs_path + "log.log", maxBytes=500, encoding='utf-8')
formatter = logging.Formatter('%(asctime)s - [%(filename)s-%(funcName)s-%(lineno)d]-%(process)d-%(processName)s\
-%(thread)d-%(threadName)s]: %(message)s')
fh.setFormatter(fmt=formatter)
fh.suffix = "%y-%m-%d.log"
fh.setLevel(logging.INFO)
logger.addHandler(fh)


