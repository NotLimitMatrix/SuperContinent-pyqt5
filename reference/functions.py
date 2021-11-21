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


def draw_text(rect: QRect, msg: str, painter: QPainter, color: QColor = None):
    if color is None:
        painter.setBrush(COLOR.BLACK)
    else:
        painter.setBrush(color)

    painter.drawText(rect, Qt.AlignHCenter | Qt.AlignVCenter, f"{msg}")
    painter.setBrush(COLOR.WHITE)


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
