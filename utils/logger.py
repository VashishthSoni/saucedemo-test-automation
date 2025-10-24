import logging
import os
from datetime import datetime

# Ensure logs directory exists
LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

def get_logger(name=__name__, log_level=logging.INFO):
    """
    Returns a configured logger object.

    :param name: Name of the logger
    :param log_level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    :return: logger instance
    """
    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    # Prevent duplicate handlers if logger is called multiple times
    if not logger.handlers:

        # Formatter for logs
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        # File handler (log file named by timestamp)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_handler = logging.FileHandler(f"{LOG_DIR}/test_{timestamp}.log", mode="w")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
