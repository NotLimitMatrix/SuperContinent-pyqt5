from PyQt5.QtWidgets import QLabel, QPushButton

from GUI import CONST


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
        name, p = info
        if name and p:
            self.label.setText(f"{info[0]}: {info[1]}")
        else:
            self.clear()
