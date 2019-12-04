from GUI import METHOD, CONST, QPainter, QColor
from GUI.Static import new_world


class World:
    def __init__(self, ws, wn):
        self.ws = ws
        self.wn = wn
        self.world_list = new_world(self.wn * self.wn)

    def update_one(self, x, y, painter: QPainter):
        painter.drawRect(x, y, self.ws, self.ws)

    def update(self, painter: QPainter):
        for index, block in enumerate(self.world_list):
            x, y = METHOD.index_to_coordinate(index, self.wn)
            pos_x, pos_y = METHOD.xy_to_position(x, y, self.ws, CONST.WORLD_POSITION_START, CONST.WORLD_POSITION_START)

            painter.setBrush(QColor(*block.color))
            self.update_one(pos_x, pos_y, painter)
            painter.setBrush(QColor(*CONST.WHITE))

        # for i in range(self.wn):
        #     for j in range(self.wn):
        #         x, y = METHOD.xy_to_position(i, j, self.ws, CONST.WORLD_POSITION_START, CONST.WORLD_POSITION_START)
        #         self.update_one(x, y, painter)
