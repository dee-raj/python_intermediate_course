import logging
logging.basicConfig(level=logging.DEBUG)
"Do basic configuration for the logging system."

logging.debug("This is a debug message")
"""
   Log a message with severity 'DEBUG' on the root logger. 
   If the logger has no handlers, call basicConfig() to add a console handler with a pre-defined format.
"""

logging.error("This is a error message")
"""
   Log a message with severity 'ERROR' on the root logger. 
   If the logger has no handlers, call basicConfig() to add a console handler with a pre-defined format.
"""

logging.warning("This is a warning message")
"""
   Log a message with severity 'WARNING' on the root logger. 
   If the logger has no handlers, call basicConfig() to add a console handler with a pre-defined format.
"""

logging.info("This is an info message")
"""
   Log a message with severity 'INFO' on the root logger. 
   If the logger has no handlers, call basicConfig() to add a console handler with a pre-defined format.
"""


logging.critical("This is a critical message")
"""
   Log a message with severity 'CRITICAL' on the root logger. 
   If the logger has no handlers, call basicConfig() to add a console handler with a pre-defined format.
"""