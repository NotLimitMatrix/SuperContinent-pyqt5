from abc import ABC

from PyQt5.QtGui import QPainter, QMouseEvent

from reference.gui import COLOR, NUMBER
from reference.functions import set_color, row_col_to_ident
from reference.game import BLOCK
from reference import dictionary
from gui.gui_base import BaseGUI


class WorldGUI(BaseGUI, ABC):
    def __init__(self, *args, **kwargs):
        super(WorldGUI, self).__init__(*args, **kwargs)
        self.n = NUMBER.WORLD_NUMBER
        self.size = self.width // NUMBER.WORLD_NUMBER
        self.world_list = None

    def draw(self, painter: QPainter, filter=dictionary.F_DEFAULT, player_color=None):
        for block in self.world_list:
            match filter:
                case dictionary.F_TERRITORY:
                    painter.setBrush(set_color(player_color, block.attribute.display))
                case dictionary.F_DEFAULT:
                    painter.setBrush(set_color(BLOCK.COLOR[block.attribute.status], block.attribute.display))
                case _:
                    painter.setBrush(COLOR.WHITE)

            rect = block.real_position(self.top, self.left)
            painter.drawRect(rect)

    def update(self, data):
        self.world_list = data

    def mouse_choose_item(self, event: QMouseEvent):
        cx = (event.pos().x() - self.left) // self.size
        cy = (event.pos().y() - self.top) // self.size
        return self.world_list[row_col_to_ident(cy, cx, self.n)]
