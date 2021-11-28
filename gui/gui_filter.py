from abc import ABC

from PyQt5.QtGui import QPainter
from PyQt5.QtCore import QRect

from reference.gui import COLOR, SIZE
from reference.functions import draw_text, tr
from reference import dictionary
from gui.gui_base import BaseGUI


class FilterUnitGUI(BaseGUI, ABC):
    def __init__(self, *args, **kwargs):
        super(FilterUnitGUI, self).__init__(*args, **kwargs)

    def update(self):
        pass

    def draw(self, name, painter: QPainter):
        painter.setBrush(COLOR.WHITE)
        rect = QRect(self.left, self.top, self.width, self.height)
        painter.drawRect(rect)
        draw_text(rect, tr(name), painter)


class FilterGUI(BaseGUI, ABC):
    def __init__(self, *args, **kwargs):
        super(FilterGUI, self).__init__(*args, **kwargs)

        self.filter_list = {
            # 默认滤镜
            dictionary.F_DEFAULT: FilterUnitGUI(
                top=self.top, left=self.left,
                width=SIZE.FILTER_ITEM_WIDTH, height=SIZE.FILTER_HEIGHT
            ),
            # 探索滤镜
            dictionary.F_DISCOVERY: FilterUnitGUI(
                top=self.top, left=self.left + SIZE.FILTER_ITEM_WIDTH,
                width=SIZE.FILTER_ITEM_WIDTH, height=SIZE.FILTER_HEIGHT
            ),
            # 领地滤镜
            dictionary.F_TERRITORY: FilterUnitGUI(
                top=self.top, left=self.left + SIZE.FILTER_ITEM_WIDTH * 2,
                width=SIZE.FILTER_ITEM_WIDTH, height=SIZE.FILTER_HEIGHT
            )
        }

    def update(self, *args, **kwargs):
        pass

    def draw(self, painter: QPainter):
        for filter, component in self.filter_list.items():
            component.draw(filter, painter)
