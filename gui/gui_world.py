from abc import ABC

from PyQt5.QtGui import QPainter

from reference.gui import COLOR, NUMBER
from reference.functions import draw_text
from reference.game import BLOCK
from gui.gui_base import BaseGUI


class WorldGUI(BaseGUI, ABC):
    def __init__(self, *args, **kwargs):
        super(WorldGUI, self).__init__(*args, **kwargs)
        self.n = NUMBER.WORLD_NUMBER
        self.size = self.width // NUMBER.WORLD_NUMBER
        self.world_list = None

    def draw(self, painter: QPainter):
        for block in self.world_list:
            if block.attribute.display:
                painter.setBrush(BLOCK.COLOR[block.attribute.status])
            else:
                painter.setBrush(COLOR.WHITE)

            rect = block.real_position(self.top, self.left)
            painter.drawRect(rect)
            draw_text(rect, f"{block.row},{block.col}", painter)

    def update(self, data):
        self.world_list = data
