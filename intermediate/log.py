import logging

logging.basicConfig(level=logging.DEBUG , format='%(asctime)s - %(name)s - %(levelname)s - %(message)s' , datefmt='%m/%d/%Y %H:%M:%S')

# Debug , info , warning , error , critical

logging.info("This is a info")
logging.debug("This is a debug")
logging.warning("This is a warning")
logging.error("This is a error")
logging.critical("This is a critical")