import logging
logger = logging.getLogger(__name__)

# create handler
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler('file.log')

# level
stream_handler.setLevel(logging.WARNING)
file_handler.setLevel(logging.ERROR)

# the format
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_f = stream_handler.setFormatter(formatter)
file_f = file_handler.setFormatter(formatter)

#add handler
logger.addHandler(stream_handler)
logger.addHandler(file_handler)


#test 
logger.warning('this is warning log')
logger.error('this is error log')