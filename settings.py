from pathlib import Path
import json

BASE_DIR = Path(__file__).parent.absolute()

USING_LANGUAGE = 'zh_cn'

with open(BASE_DIR.joinpath('localization').joinpath(f"{USING_LANGUAGE}.json"), 'r', encoding='utf-8') as f:
    LANGUAGE_DICTIONARY: dict = json.load(f)
