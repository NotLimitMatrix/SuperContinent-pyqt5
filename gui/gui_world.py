from abc import ABC

from PyQt5.QtGui import QPainter, QMouseEvent

from reference.gui import COLOR, NUMBER
from reference.functions import draw_text, row_col_to_ident
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
            color = COLOR.WHITE
            if filter == dictionary.F_TERRITORY:
                color = player_color if block.attribute.display and player_color is not None else COLOR.WHITE
            if filter == dictionary.F_DEFAULT:
                color = BLOCK.COLOR[block.attribute.status] if block.attribute.display else COLOR.WHITE

            painter.setBrush(color)
            # if block.attribute.display:
            #     painter.setBrush(BLOCK.COLOR[block.attribute.status])
            # else:
            #     painter.setBrush(COLOR.WHITE)

            rect = block.real_position(self.top, self.left)
            painter.drawRect(rect)
            # draw_text(rect, f"{block.row},{block.col}", painter)

    def update(self, data):
        self.world_list = data

    def mouse_choose_item(self, event: QMouseEvent):
        cx = (event.pos().x() - self.left) // self.size
        cy = (event.pos().y() - self.top) // self.size
        return self.world_list[row_col_to_ident(cy, cx, self.n)]
