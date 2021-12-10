import json
import zlib
import random
import string

from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QColor, QPainter

from reference.gui import COLOR
from settings import LANGUAGE_DICTIONARY

JSONEncoder = json.JSONEncoder()
JSONDecoder = json.JSONDecoder()


def row_col_to_ident(row, col, number):
    return row * number + col


def ident_to_row_col(ident, number):
    return divmod(ident, number)


def game_time_to_date(time_number):
    days = time_number % 30 + 1
    months = (time_number // 30) % 12 + 1
    years = time_number // 360
    return f"{years + 1}-{'' if months > 9 else '0'}{months}-{'' if days > 9 else '0'}{days}"


def draw_text(rect: QRect, msg: str, painter: QPainter, color: QColor = None):
    if color is None:
        painter.setPen(COLOR.BLACK)
    else:
        painter.setPen(color)

    painter.drawText(rect, Qt.AlignHCenter | Qt.AlignVCenter, f"{msg}")
    painter.setPen(COLOR.BLACK)


def compress_string(s: str):
    return zlib.compress(s.encode('utf-8'))


def decompress_string(s):
    return zlib.decompress(s).decode('utf-8')


def compress_dict(s):
    temp = ''.join(JSONEncoder.encode(s))
    return zlib.compress(zlib.compress(temp.encode('utf-8')))


def decompress_dict(s):
    return JSONDecoder.decode(zlib.decompress(zlib.decompress(s)).decode('utf-8'))


def tr(msg):
    return LANGUAGE_DICTIONARY.get(msg, msg)


def fmt_number(number):
    n = abs(number)
    if n > 1000000000:
        return f"{round(number / 1000000000, 2)} G"
    elif n > 999999:
        return f"{round(number / 1000000, 2)} M"
    elif n > 999:
        return f"{round(number / 1000, 2)} K"
    else:
        return str(number)


def weight_choice(weights: tuple):
    temp = random.uniform(0, sum(weights) - 1)
    for index, value in enumerate(weights):
        temp -= value
        if temp < 0:
            return index


def set_color(color, display):
    if color is None or not display:
        return COLOR.WHITE
    else:
        return color
