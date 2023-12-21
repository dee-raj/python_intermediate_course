import logging

logger = logging.getLogger(__name__) 

# logger.propagate = False
logger.info('hello from my logger')

logger.critical(f'critical message from {__name__}')