from abc import abstractmethod, ABC

from PyQt5.QtGui import QMouseEvent


class BaseGUI(ABC):
    def __init__(self, top, left, width, height, parent):
        self.top = top
        self.left = left
        self.width = width
        self.height = height
        self.parent = parent

    @abstractmethod
    def update(self, *args, **kwargs):
        """更新界面"""

    def in_this(self, event: QMouseEvent):
        pos = event.pos()
        bool_x = self.left <= pos.x() <= self.left + self.width
        bool_y = self.top <= pos.y() <= self.top + self.height
        return bool_x and bool_y
