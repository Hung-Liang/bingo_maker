import logging
from pathlib import Path

from lib.file_path import LOG_PATH


def log(message: str = '', console: bool = False):
    '''Basic Log to Record Progress.

    Args:
        message: Logging message.
    '''

    file_path = Path(LOG_PATH, 'log.log')

    handlers = logging.FileHandler(
        filename=str(file_path), encoding='utf-8', mode='a'
    )
    logging.basicConfig(
        format='%(asctime)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        handlers=[handlers],
    )

    logging.error(message)

    if console:
        print(message)
