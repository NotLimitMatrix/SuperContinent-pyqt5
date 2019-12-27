from Core import CONST
from GUI.GUI_shape import Shape


class Block:
    def __init__(self, ident, status_id, zn, ws, ids: tuple):
        # 地块环境 (0:绝地 1:恶劣 2:一般 3:良好 4:理想)
        self.id = ident
        self.status_id = status_id
        self.color = CONST.BLOCK_STATUS_COLOR[status_id]
        self.observable = True
        self.zoning_number = zn
        self.ids = ids
        self.ws = ws

        # 0:None, 1:探索者(圆) 2:部队(三角形)
        self.solt1 = Shape(0, self.ws // 2)
        self.solt2 = Shape(0, self.ws // 2)

    def draw_solt(self, painter):
        dy, dx = self.ids
        self.solt1.draw(painter, dx * self.ws, dy * self.ws)
        self.solt2.draw(painter, dx * self.ws + self.ws // 2, dy * self.ws)

    def clear_color(self):
        self.color = CONST.BLOCK_STATUS_COLOR[self.status_id]

    def set_color(self, color):
        self.color = color

    def display(self):
        produce = CONST.BLOCK_MODIFIER[self.status_id]
        produce_modifier = f"+{produce}%" if produce > 0 else f"{produce}%"

        upkeep = -produce
        upkeep_modifier = f"+{upkeep}%" if upkeep > 0 else f"{upkeep}%"

        temp = f"""地块: {self.id}
环境：{CONST.BLOCK_WORD[self.status_id]} {CONST.BLOCK_PERCENT[self.status_id]}%
生产修正: {produce_modifier}
维护花费: {upkeep_modifier}
"""
        return temp
