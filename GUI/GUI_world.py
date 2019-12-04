from GUI import METHOD, CONST, QPainter


class World:
    def __init__(self, ws, wn):
        self.ws = ws
        self.wn = wn
        self.world_list = []

    def update_one(self, x, y, painter: QPainter):
        painter.drawRect(x, y, self.ws, self.ws)

    def update(self, painter: QPainter):
        for i in range(self.wn):
            for j in range(self.wn):
                x, y = METHOD.xy_to_position(i, j, self.ws, CONST.WORLD_POSITION_START, CONST.WORLD_POSITION_START)
                self.update_one(x, y, painter)
