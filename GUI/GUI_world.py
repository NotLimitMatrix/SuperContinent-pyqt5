from GUI import METHOD, CONST, QPainter, QColor
from GUI.Static import new_world


class World:
    def __init__(self, ws, wn):
        self.ws = ws
        self.wn = wn
        self.world_list = new_world(self.wn * self.wn)

    def update_one(self, x, y, painter: QPainter, block):
        if block.observable:
            painter.setBrush(QColor(*block.color))
        else:
            painter.setBrush(QColor(*CONST.White))

        painter.drawRect(x, y, self.ws, self.ws)
        painter.setBrush(QColor(*CONST.White))

    def update(self, painter: QPainter):
        for index, block in enumerate(self.world_list):
            x, y = METHOD.index_to_coordinate(index, self.wn)
            pos_x, pos_y = METHOD.xy_to_position(x, y, self.ws, CONST.WORLD_POSITION_START, CONST.WORLD_POSITION_START)

            print(block.id, block.status_id)

            self.update_one(pos_x, pos_y, painter, block)
