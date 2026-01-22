import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path


import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path


def setup_logging(log_level: str = "INFO", log_dir: str = "logs") -> None:
    """
    Configure logging to FILE ONLY (no console output).
    """
    Path(log_dir).mkdir(parents=True, exist_ok=True)

    log_format = (
        "%(asctime)s | %(levelname)s | "
        "%(name)s | %(funcName)s | %(message)s"
    )

    formatter = logging.Formatter(log_format)

    file_handler = RotatingFileHandler(
        filename=f"{log_dir}/triage.log",
        maxBytes=5_000_000,   # 5 MB
        backupCount=3,
    )
    file_handler.setFormatter(formatter)

    # IMPORTANT: clear existing handlers (prevents duplicates)
    root_logger = logging.getLogger()
    root_logger.handlers.clear()

    root_logger.setLevel(
        getattr(logging, log_level.upper(), logging.INFO)
    )
    root_logger.addHandler(file_handler)

    # Optional: reduce noise from third-party libraries
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    logging.getLogger("openai").setLevel(logging.WARNING)

