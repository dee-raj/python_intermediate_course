import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)

handler = RotatingFileHandler('app.log', maxBytes=200, backupCount=4)
logger.addHandler(handler)

for _ in range(100):
   logger.info('Hello world!')
   pass


# Time rotating File handler
from logging.handlers import TimedRotatingFileHandler
import time
time_handler = TimedRotatingFileHandler('timed_test.log', when='s', interval=5, backupCount=5)
'where => s=second, m=minute, h=hour, midnight, w0=monday, w1=tuesday...w7=satarday'
logger.addHandler(time_handler)

for _ in range(6):
   logger.info('Hello world!')
   time.sleep(5)