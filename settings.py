from pathlib import Path
import json

BASE_DIR = Path(__file__).parent.absolute()

USING_LANGUAGE = 'cn'

LANGUAGE_FILE = BASE_DIR.joinpath('localization').joinpath(f"{USING_LANGUAGE}.json")
if LANGUAGE_FILE.exists():
    with open(LANGUAGE_FILE, 'r', encoding='utf-8') as f:
        LANGUAGE_DICTIONARY: dict = json.load(f)
else:
    LANGUAGE_DICTIONARY = dict()

SPEED = 1
TIME_FLOW = 1 / SPEED
