from abc import abstractmethod, ABC

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QRect, Qt

from reference.gui import COLOR


class BaseGUI(ABC):
    def __init__(self, top, left, width, height):
        self.top = top
        self.left = left
        self.width = width
        self.height = height

    @abstractmethod
    def update(self, *args, **kwargs):
        """更新界面"""

    @abstractmethod
    def draw_component(self, painter: QPainter):
        """绘制界面"""
