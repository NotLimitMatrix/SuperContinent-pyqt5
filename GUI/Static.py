from GUI import (
    QTableWidget,
    QTableWidgetItem,
    QFont,
    Qt
)


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

    return table