from abc import ABC

from PyQt5.QtGui import QPainter, QMouseEvent
from PyQt5.QtCore import QRect

from reference.gui import COLOR, SIZE
from reference.functions import draw_text, tr
from reference import dictionary
from reference.templates import TEMPLATE_FILTER
from gui.gui_base import BaseGUI


class FilterUnitGUI(BaseGUI, ABC):
    def __init__(self, name, *args, **kwargs):
        super(FilterUnitGUI, self).__init__(*args, **kwargs)
        self.name = name

    def update(self):
        pass

    def draw(self, painter: QPainter):
        painter.setBrush(COLOR.WHITE)
        rect = QRect(self.left, self.top, self.width, self.height)
        painter.drawRect(rect)
        draw_text(rect, tr(self.name), painter)

    def display(self):
        return TEMPLATE_FILTER.format(
            filter_type=tr(self.name)
        )


class FilterGUI(BaseGUI, ABC):
    def __init__(self, *args, **kwargs):
        super(FilterGUI, self).__init__(*args, **kwargs)

        self.filter_list = [
            # 默认滤镜
            FilterUnitGUI(dictionary.F_DEFAULT, top=self.top, left=self.left,
                          width=SIZE.FILTER_ITEM_WIDTH, height=SIZE.FILTER_HEIGHT),
            # 探索滤镜
            FilterUnitGUI(dictionary.F_DISCOVERY, top=self.top, left=self.left + SIZE.FILTER_ITEM_WIDTH,
                          width=SIZE.FILTER_ITEM_WIDTH, height=SIZE.FILTER_HEIGHT),
            # 领地滤镜
            FilterUnitGUI(dictionary.F_TERRITORY, top=self.top, left=self.left + SIZE.FILTER_ITEM_WIDTH * 2,
                          width=SIZE.FILTER_ITEM_WIDTH, height=SIZE.FILTER_HEIGHT)
        ]

    def update(self, *args, **kwargs):
        pass

    def draw(self, painter: QPainter):
        for component in self.filter_list:
            component.draw(painter)

    def mouse_choose_item(self, event: QMouseEvent):
        return self.filter_list[(event.pos().x() - self.left) // SIZE.FILTER_ITEM_WIDTH]
