from GUI import METHOD, CONST, QPainter, CONST, QRect, Qt


class Zoning:
    def __init__(self, zs, zn):
        self.zs = zs
        self.zn = zn
        self.zoning_list = []

    def set_number(self, n):
        self.zn = n
        self.zs = CONST.ZONING_WIDTH // n

    def update_one(self, x, y, painter: QPainter, n):
        painter.drawRect(x, y, self.zs, self.zs)

        # 这段代码开发时使用，用于显示区划的序号
        painter.drawText(QRect(x, y, self.zs, self.zs), Qt.AlignHCenter | Qt.AlignVCenter, str(n))
        #

    def update(self, painter: QPainter):
        for i in range(self.zn):
            for j in range(self.zn):
                x, y = METHOD.xy_to_position(i, j, self.zs, CONST.ZONING_POSITION_START_X,
                                             CONST.ZONING_POSITION_START_Y)

                self.update_one(x, y, painter, i + j * self.zn)
