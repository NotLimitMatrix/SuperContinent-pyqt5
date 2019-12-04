from Core.CONST import BLOCK_STATUS_COLOR


class Block:
    def __init__(self, ident, status_id):
        # 地块环境 (0:绝地 1:恶劣 2:一般 3:良好 4:理想)
        self.id = ident
        self.status_id = status_id
        self.color = BLOCK_STATUS_COLOR[status_id]
