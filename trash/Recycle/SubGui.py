from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QLabel, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

from Recycle.static import CONST


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


class OneResearchPanel:
    def __init__(self, parent):
        self.parent = parent

        self.label = QLabel(self.parent)
        self.rate_button = QPushButton(self.parent)
        self.transform_button = QPushButton(self.parent)

    def init_label(self, x, y):
        self.label.setGeometry(x, y, 100, 18)
        self.label.setStyleSheet(CONST.RESEARCH_LABEL_STYLE)
        self.label.setText("没有研究")

    def init_rate_button(self, x, y):
        self.rate_button.setGeometry(x, y, 30, 30)
        self.rate_button.setText('')
        self.rate_button.clicked.connect(self.update_rate)

    def init_transform_button(self, x, y):
        self.transform_button.setGeometry(x, y, 30, 30)
        self.transform_button.setText('T')
        self.transform_button.clicked.connect(self.update_transform)

    def update_rate(self):
        pass

    def update_transform(self):
        pass

    def clear(self):
        self.label.setText("没有研究")

    def display(self, info: tuple):
        if info:
            self.label.setText(f"{info[0]}: {info[1]}")
        else:
            self.clear()
