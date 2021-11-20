from abc import abstractmethod, ABC

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QRect, Qt

from reference.gui import COLOR


class BaseGUI(ABC):
    def __init__(self, width, height, painter: QPainter):
        self.width = width
        self.height = height
        self.painter = painter

    @abstractmethod
    def update(self):
        """更新界面"""

    def draw_text(self, rect: QRect, color: QColor, msg: str):
        self.painter.setBrush(color)
        self.painter.drawText(rect, Qt.AlignHCenter | Qt.AlignVCenter, msg)
        self.painter.setBrush(COLOR.WHITE)
