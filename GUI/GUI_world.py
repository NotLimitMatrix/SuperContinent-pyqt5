from GUI import METHOD, CONST, QPainter, QColor, QRect, Qt
from GUI.Static import new_world
from GUI.GUI_shape import Shape


class World:
    def __init__(self, ws, wn):
        self.ws = ws
        self.wn = wn
        self.world_list = new_world(self.wn)

    def update_one(self, x, y, painter: QPainter, block):
        if block.observable:
            painter.setBrush(QColor(*block.color))
        else:
            painter.setBrush(QColor(*CONST.White))

        painter.drawRect(x, y, self.ws, self.ws)

        # 这段代码开发时使用，用于显示地块的序号
        painter.drawText(QRect(x, y, self.ws, self.ws), Qt.AlignHCenter | Qt.AlignVCenter, str(block.ids))
        #
        painter.setBrush(QColor(*CONST.Black))
        block.draw_solt(painter)
        painter.setBrush(QColor(*CONST.White))

    def block(self, index):
        return self.world_list[index]

    def update(self, painter: QPainter):
        for index, block in enumerate(self.world_list):
            pos_x, pos_y = METHOD.index_to_pos_xy(index, self.wn, self.ws, CONST.WORLD_POSITION_START,
                                                  CONST.WORLD_POSITION_START)

            self.update_one(pos_x, pos_y, painter, block)
