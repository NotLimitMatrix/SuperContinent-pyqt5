from GUI import (
    CONST,
    QListWidget,
    QListWidgetItem,
    QAbstractItemView,
    QSize,
)
from trash.STATIC import KEY

from GUI.ItemWidget import TechnologyItemWidget


class WaitSelect:
    def __init__(self, parent):
        wsw = QListWidget(parent)
        wsw.setGeometry(CONST.WAIT_PANEL_START_X, CONST.WAIT_PANEL_START_Y,
                        CONST.WAIT_PANEL_WIDTH, CONST.WAIT_PANEL_HEIGHT)
        wsw.setStyleSheet("QListWidget{border:1px solid black; color:black; }"
                          "QListWidget::Item{padding-top:0px; padding-bottom:4px; }")
        wsw.setSelectionMode(QAbstractItemView.NoSelection)

        self.wait_select = wsw
        self.wait_select_items = []

    def check_items(self, items: list):
        if items is None or items == self.wait_select_items:
            return True

        self.wait_select_items = items.copy()
        if self.wait_select_items:
            return False
        else:
            return True

    def update(self, items: list):
        if self.check_items(items):
            return

        self.wait_select.clear()

        for item in self.wait_select_items:
            option_item = QListWidgetItem()
            option_item.setSizeHint(QSize(200, 120))

            W = TechnologyItemWidget(t=KEY.TECHNOLOGY, datas=item).to_widget()
            self.wait_select.addItem(option_item)
            self.wait_select.setItemWidget(option_item, W)
