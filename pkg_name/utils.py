"""
Common utilities used across modules.
"""

# %% ../nbs/99_utils.ipynb 0
import logging
from typing import Optional


def get_logger(
    name: str,
    fmt: str = "[%(levelname)s] [%(asctime)s.%(msecs)d] [pid %(process)d] [%(pathname)s:%(lineno)d:%(funcName)s]\n%(message)s",
    datefmt: str = "%Y-%m-%d %H:%M:%S",
    level: int = logging.INFO,
    log_path: Optional[str] = None,
    file_mode: str = "w",
) -> logging.Logger:
    """
    Get a configured logger.

    Parameters
    ----------
    name: str
        Name of the logger.
    fmt: str
        Format of the log message.
    datefmt: str
        Date format of the log message.
    level: int
        Level of the log message.
    log_path: Optional[str]
        Path to the log file.
    file_mode: str
        Mode of the log file.

    Returns
    -------
    logging.Logger
        Configured logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Remove any existing handlers
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

    # Create formatter
    formatter = logging.Formatter(fmt=fmt, datefmt=datefmt)

    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Create file handler if log_path is provided
    if log_path is not None:
        file_handler = logging.FileHandler(log_path, mode=file_mode)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.info(f"log_path = {log_path}")

    return logger


if __name__ == "__main__":
    logger = get_logger(__name__)
    logger.info("Test logging.")
