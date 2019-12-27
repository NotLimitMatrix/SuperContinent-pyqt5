from GUI import (
    QTableWidget,
    QTableWidgetItem,
    QAbstractItemView,
    QFont,
    Qt,
    QPainter,
    QPolygon,
)

from Core.CONST import WORLD_WIDTH

from Core.METHOD import RandomBlock, square_from_one_xy, xy_to_index
from Block import Block


def draw_ellipse(painter: QPainter, x, y, ws):
    painter.drawEllipse(x + ws // 4, y + ws // 4, ws // 2, ws // 2)


def draw_three_angle(painter: QPainter, x, y, ws):
    polygon = QPolygon()
    polygon.setPoints(x + ws // 2, y + ws // 6, x + ws // 6, y + 5 * ws // 6, x + 5 * ws // 6, y + 5 * ws // 6)
    painter.drawPolygon(polygon)


def draw_which(painter: QPainter, _type, x, y, ws):
    if _type == 0:
        return
    if _type == 1:
        draw_ellipse(painter, x, y, ws)
    if _type == 2:
        draw_three_angle(painter, x, y, ws)


def draw_solt(painter: QPainter, solt1, solt2, px, py, ws):
    draw_which(painter, solt1, px, py, ws // 2)
    draw_which(painter, solt2, px + ws // 2, py, ws // 2)


def GenerateTable(parent, r, c, hSize, vSize):
    table = QTableWidget(parent)
    table.setRowCount(r)
    table.setColumnCount(c)
    table.horizontalHeader().setVisible(False)
    table.horizontalHeader().setDefaultSectionSize(hSize)
    table.horizontalHeader().setHighlightSections(False)
    table.verticalHeader().setVisible(False)
    table.verticalHeader().setDefaultSectionSize(vSize)
    table.verticalHeader().setHighlightSections(False)

    font = QFont()
    font.setPixelSize(11)

    for r_ in range(r):
        for c_, item in enumerate(QTableWidgetItem() for _ in range(c)):
            item.setTextAlignment(Qt.AlignCenter)
            item.setFont(font)
            table.setItem(r_, c_, item)

    # 设置 不可编辑
    table.setEditTriggers(QAbstractItemView.NoEditTriggers)
    # 设置 不可选择
    table.setSelectionMode(QAbstractItemView.NoSelection)

    return table


def new_world(size):
    rb = RandomBlock()
    ws = WORLD_WIDTH // size
    b_list = []
    for i, b in enumerate(rb.new_world(size * size)):
        status_id, zoning_number = b
        ids = divmod(i, size)
        b_list.append(Block(i, status_id, zoning_number, ws, ids))

    return b_list