from GUI import (
    QTableWidget,
    QTableWidgetItem,
    QAbstractItemView,
    QFont,
    Qt,
)

from Core.METHOD import RandomBlock
from Block import Block


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
    b_list = []
    for i, b in enumerate(rb.new_world(size)):
        status_id, zoning_number = b
        b_list.append(Block(i, status_id, zoning_number))
    return b_list
