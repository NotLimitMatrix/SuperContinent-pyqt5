from PyQt5.QtWidgets import (
    QLabel,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
)

from static import KEY


class ItemWidget:
    def __init__(self, t, datas):
        self.type = t
        self.datas = datas

    def to_widget(self, *args, **kwargs):
        pass


class TechnologyItemWidget(ItemWidget):
    def to_widget(self):
        if self.type != KEY.TECHNOLOGY:
            raise ValueError("备选列表类型错误")

        name, cost, info = self.datas

        name_label = QLabel(name)
        cost_label = QLabel(str(cost))
        line_label = QLabel('----------------------')

        if len(info) > 3:
            raise ValueError("科技描述信息不能超过3条")
        info_label = QLabel('\n'.join(info))

        main_layout = QVBoxLayout()
        top_layout = QHBoxLayout()

        top_layout.addWidget(name_label)
        top_layout.addWidget(cost_label)

        main_layout.addLayout(top_layout)
        main_layout.addWidget(line_label)
        main_layout.addWidget(info_label)

        widget = QWidget()
        widget.setLayout(main_layout)
        widget.setStyleSheet("background-color:rgb(176,196,222)")
        return widget
