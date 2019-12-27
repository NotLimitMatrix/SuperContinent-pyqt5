from GUI import METHOD, CONST, QPainter, QColor, QRect, Qt
from GUI.Static import new_world
from Core.METHOD import Vector


class World:
    def __init__(self, ws, wn):
        self.ws = ws
        self.wn = wn
        self.world_list = new_world(self.wn)

    def update_one(self, x, y, painter: QPainter, block):
        if block.observable:
            painter.setBrush(QColor(*block.color))
        else:
            painter.setBrush(QColor(*CONST.DimGrey))

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

    def AStar_path(self, x1, y1, x2, y2):
        d = -1
        closedset = [(x1, y1)]
        openset = [(i, j) for i in range(self.wn) for j in range(self.wn)]
        openset.remove((x1, y1))

    def square_from_one_xy(self, x, y, sn):
        if sn > self.wn:
            raise ValueError("步长不能大于地图尺寸")
        sn += 1
        d = [i for i in range(sn)]
        left_x = [(0 if x - i < 0 else x - i) for i in d]
        right_x = [(self.wn - 1 if x + i >= self.wn else x + i) for i in d]
        xs = set(left_x + right_x)
        left_y = [(0 if y - i < 0 else y - i) for i in d]
        right_y = [((self.wn - 1) if y + i >= self.wn else y + i) for i in d]
        ys = set(left_y + right_y)
        points = [Vector(i, j) for i in xs for j in ys]

        return [point for point in points if self.block_can_move_with_point(point)]

    def square_from_one_walk(self, x, y):
        lx = 0 if x - 1 < 0 else x - 1
        gx = self.wn - 1 if x + 1 == self.wn else x + 1
        ly = 0 if y - 1 < 0 else y - 1
        gy = self.wn - 1 if y + 1 == self.wn else y + 1

        points = [Vector(x, y), Vector(lx, y), Vector(gx, y), Vector(x, ly), Vector(x, gy)]
        return [point for point in set(points) if self.block_can_move_with_point(point)]

    def block_can_move_with_index(self, block_id):
        return self.block(block_id).can_move

    def block_can_move_with_point(self, point: Vector):
        return self.block_can_move_with_index(METHOD.xy_to_index(point.x, point.y, self.wn))
