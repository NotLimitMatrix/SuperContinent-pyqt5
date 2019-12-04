from GUI import METHOD, CONST, QPainter


class Zoning:
    def __init__(self, zs, zn):
        self.zs = zs
        self.zn = zn
        self.zoning_list = []

    def update_one(self, x, y, painter: QPainter):
        painter.drawRect(x, y, self.zs, self.zs)

    def update(self, painter: QPainter):
        for i in range(self.zn):
            for j in range(self.zn):
                x, y = METHOD.from_xy_to_position(i, j, self.zs, CONST.ZONING_POSITION_START_X,
                                                  CONST.ZONING_POSITION_START_Y)
                self.update_one(x, y, painter)
