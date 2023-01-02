import os
from pathlib import Path

from lib.config import config

PROGRAM_PATH = os.path.dirname(os.path.dirname(__file__))

LOG_PATH = Path(PROGRAM_PATH, 'log')
OUTPUT_PATH = Path(PROGRAM_PATH, 'output')
BINGO_PATH = Path(PROGRAM_PATH, 'bingo_sheet')
ASSET_PATH = Path(PROGRAM_PATH, 'asset')
FONT_PATH = Path(ASSET_PATH, config["font_name"])
TEXT_PATH = Path(ASSET_PATH, 'text_list.txt')

LOG_PATH.mkdir(parents=True, exist_ok=True)
OUTPUT_PATH.mkdir(parents=True, exist_ok=True)
BINGO_PATH.mkdir(parents=True, exist_ok=True)
