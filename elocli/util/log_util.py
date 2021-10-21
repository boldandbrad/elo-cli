
from loguru import logger

from .env_util import get_log_path


def log_init() -> None:
    """Configure loguru logger.
    """

    logger.remove()  # remove stdout/stderr logging since this is a CLI

    log_path = get_log_path()
    log_format = '{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}'

    logger.add(
        log_path + 'elo.log', format=log_format, compression='zip', retention='1 day'
    )
