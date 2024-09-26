"""
Common utilities used across modules.
"""

import logging
from typing import Optional


# %% ../nbs/99_utils.ipynb 0
def init_logging(
    fmt: str = "[%(levelname)s] [%(asctime)s.%(msecs)d] [pid %(process)d] [%(pathname)s:%(lineno)d:%(funcName)s]\n%(message)s",
    datefmt: str = "%Y-%m-%d %H:%M:%S",
    level: int = logging.INFO,
    log_path: Optional[str] = None,
    file_mode: str = "w",
    force: bool = True,
) -> None:
    """
    Initialize logging.

    Parameters
    ----------
    format: str
        Format of the log message.
    datefmt: str
        Date format of the log message.
    level: int
        Level of the log message.
    log_path: Optional[str]
        Path to the log file.
    file_mode: str
        Mode of the log file.
    force: bool
        Whether to force the logging to be initialized.
    """
    if force:
        logging.shutdown()

    logging.basicConfig(
        format=fmt,
        datefmt=datefmt,
        level=level,
        force=force,
    )

    if log_path is not None:
        file_handler = logging.FileHandler(log_path, mode=file_mode)
        file_handler.setLevel(level)
        file_handler.setFormatter(logging.Formatter(fmt=fmt, datefmt=datefmt))

        logging.getLogger().addHandler(file_handler)
        logging.info(f"log_path = {log_path}")


init_logging()
logging.info("Test logging.")
