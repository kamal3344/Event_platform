import logging

def setup_logging():
    # Create a logger object
    logger = logging.getLogger(__name__)

    # Set the logging level
    logger.setLevel(logging.DEBUG)

    # Create a file handler
    handler = logging.FileHandler('D:\\Event_platform\\logs\\configuration.log')

    # Create a formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Set the formatter for the handler
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)

    return logger


