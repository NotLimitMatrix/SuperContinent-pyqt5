from abc import ABC

from PyQt5.QtGui import QPainter, QMouseEvent
from PyQt5.QtCore import QRect

from reference.gui import COLOR, SIZE
from reference.game import OPTIONS
from reference.functions import draw_text, tr
from gui.gui_base import BaseGUI


class ConsoleItemGUI(BaseGUI, ABC):
    def __init__(self, name, using, *args, **kwargs):
        super(ConsoleItemGUI, self).__init__(*args, **kwargs)
        self.name = name
        self.using = using

    def update(self):
        pass

    def draw(self, painter: QPainter):
        painter.setBrush(COLOR.WHITE)
        rect = QRect(self.left, self.top, self.width, self.height)
        painter.drawRect(rect)
        draw_text(rect, tr(self.name), painter)

    def display(self):
        return tr(self.name)


class ConsoleGUI(BaseGUI, ABC):
    def __init__(self, *args, **kwargs):
        super(ConsoleGUI, self).__init__(*args, **kwargs)

        self.console_list = [
            ConsoleItemGUI(item, True, top=self.left, left=self.left + index * SIZE.TOOL_ITEM_WIDTH,
                           width=SIZE.TOOL_ITEM_WIDTH, height=SIZE.TOOL_ITEM_HEIGHT, parent=self.parent)
            for index, item in enumerate(OPTIONS.TOOLS)
        ]

    def update(self, *args, **kwargs):
        pass

    def draw(self, painter: QPainter):
        for component in self.console_list:
            component.draw(painter)

    def mouse_choose_item(self, event: QMouseEvent):
        try:
            return self.console_list[(event.pos().x() - self.left) // SIZE.TOOL_ITEM_WIDTH]
        except Exception as e:
            return None
