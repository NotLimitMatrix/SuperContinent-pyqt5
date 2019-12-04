from Core import CONST


class Block:
    def __init__(self, ident, status_id, zn):
        # 地块环境 (0:绝地 1:恶劣 2:一般 3:良好 4:理想)
        self.id = ident
        self.status_id = status_id
        self.color = CONST.BLOCK_STATUS_COLOR[status_id]
        self.observable = True
        self.zoning_number = zn

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
