# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'superv1.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QAbstractItemView


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.init(Dialog)
        self.bottons = self.init_buttons(Dialog)
        self.tech_bottons = self.technologist_buttons(Dialog)
        self.tech_labels = self.technologist_labels(Dialog)
        self.resource_panel = self.resource_table_view(Dialog)
        self.technology_panel = self.cs_table_view(Dialog)
        self.select_list = self.select_list_view(Dialog)

        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(850, 315, 148, 285))
        self.textBrowser.setObjectName("textBrowser")

    def init(self, dialog):
        dialog.resize(1000, 600)
        dialog.setMinimumSize(QtCore.QSize(1000, 600))
        dialog.setMaximumSize(QtCore.QSize(1000, 600))
        dialog.setWindowTitle("SuperContinent")

    def init_buttons(self, dialog):
        _list = []

        # 这段代码毫无意义，但是如果不加上，第一个按钮有点不一样，强迫症表示很不舒服。如果你测试的时候没有其他情况，可能是我脸比较黑
        temp = QtWidgets.QPushButton(dialog)
        temp.setGeometry(0, 0, 0, 0)
        temp.setText('')
        ##########

        for i in range(6):
            for j in range(6):
                b = QtWidgets.QPushButton(dialog)

                x = 600 + j * 40
                y = 0 + i * 40

                b.setGeometry(x, y, 50, 50)
                b.setText('')
                _list.append(b)

        return _list

    def technologist_buttons(self, dialog):
        X_base = 950
        X_instance = 20

        tech_buttons = [
            (0, 250), (1, 250),
            (0, 270), (1, 270),
            (0, 290), (1, 290)
        ]
        _dict = {
            'military': {'rate': None, 'T': None},
            'civil': {'rate': None, 'T': None},
            'beyond': {'rate': None, 'T': None}
        }
        keys = [val for val in _dict.keys() for i in range(2)]

        for (x, y), key in zip(tech_buttons, keys):
            b = QtWidgets.QPushButton(dialog)
            b.setGeometry(X_base + X_instance * x, y, 30, 30)
            b.setText('T' if x else ('4' if y == 290 else '3'))

            _dict[key]['T' if x else 'rate'] = b

        return _dict

    def technologist_labels(self, dialog):
        _dict = {
            'military': None,
            'civil': None,
            'beyond': None
        }
        X_base = 850
        Y_base = 256
        Y = [Y_base + i * 20 for i in range(3)]

        style = "font: 10pt ;border-width: 1px;border-style: solid;border-color: rgb(0, 0, 0)"

        for k, y in zip(_dict.keys(), Y):
            label = QtWidgets.QLabel(dialog)
            label.setGeometry(X_base, y, 100, 18)
            label.setStyleSheet(style)
            label.setText(f"未选科技：{k}")

            _dict[k] = label

        return _dict

    def gen_table(self, dialog, row, col, h_size, v_size):
        table = QtWidgets.QTableWidget(dialog)

        table.setRowCount(row)
        table.setColumnCount(col)
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        table.setSelectionMode(QAbstractItemView.NoSelection)

        table.horizontalHeader().setVisible(False)
        table.horizontalHeader().setDefaultSectionSize(h_size)
        table.horizontalHeader().setHighlightSections(False)
        table.verticalHeader().setVisible(False)
        table.verticalHeader().setDefaultSectionSize(v_size)
        table.verticalHeader().setHighlightSections(False)

        for r in range(row):
            for c, item in enumerate(QtWidgets.QTableWidgetItem() for _ in range(col)):
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                table.setItem(r, c, item)

        return table

    def resource_table_view(self, dialog):
        table = self.gen_table(dialog, 5, 3, 48, 26)
        table.setGeometry(850, 3, 148, 135)

        panels = [
            ('能量', '24K', '+1K'),
            ('矿物', '12K', '-2K'),
            ('食物', '10M', '+3K'),
            ('物资', '2K', '-241'),
            ('合金', '1K', '+328')
        ]

        for row in range(5):
            for col in range(3):
                item = table.item(row, col)
                item.setText(panels[row][col])
        return table

    def cs_table_view(self, dialog):
        table = self.gen_table(dialog, 3, 2, 73, 36)
        table.setGeometry(850, 140, 148, 110)

        panels = [
            ('经济', '18203'),
            ('军事', '39281'),
            ('科研', '49K')
        ]

        for row in range(3):
            for col in range(2):
                item = table.item(row, col)
                item.setText(panels[row][col])
        return table

    def select_list_view(self, dialog):
        listView = QtWidgets.QListView(dialog)
        listView.setGeometry(607, 250, 237, 350)
        return listView


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = QDialog()
    dlg = Ui_Dialog()
    dlg.setupUi(form)
    form.show()
    sys.exit(app.exec_())
