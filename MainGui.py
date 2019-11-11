import sys, time

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QTableWidget,
    QTableWidgetItem,
    QAbstractItemView,
    QListWidget,
    QListWidgetItem,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
)
from PyQt5.QtCore import (
    QObject,
    pyqtSignal,
    Qt,
    QRect,
    QSize,
)
from PyQt5.QtGui import (
    QPainter,
    QPen,
    QColor,
    QBrush,
    QFont,
)

from static import *


def get_wait_item_widget(name, cost, informations):
    name_label = QLabel(name)
    cost_label = QLabel(str(cost))
    line_label = QLabel("----------------------")

    if len(informations) > 2:
        info_label = QLabel(f"{informations[0]}\n{informations[1]}\n......")
    else:
        info_label = QLabel('\n'.join(informations))

    widget = QWidget()

    main_layout = QVBoxLayout()
    top_layout = QHBoxLayout()

    top_layout.addWidget(name_label)
    top_layout.addWidget(cost_label)

    main_layout.addLayout(top_layout)
    main_layout.addWidget(line_label)
    main_layout.addWidget(info_label)

    widget.setLayout(main_layout)
    widget.setStyleSheet("background-color:rgb(176,196,222)")
    return widget


def generate_table(parent, row, col, h_size, v_size):
    table = QTableWidget(parent)
    table.setRowCount(row)
    table.setColumnCount(col)
    table.horizontalHeader().setVisible(False)
    table.horizontalHeader().setDefaultSectionSize(h_size)
    table.horizontalHeader().setHighlightSections(False)
    table.verticalHeader().setVisible(False)
    table.verticalHeader().setDefaultSectionSize(v_size)
    table.verticalHeader().setHighlightSections(False)

    font = QFont()
    font.setPixelSize(11)

    for r in range(row):
        for c, item in enumerate(QTableWidgetItem() for _ in range(col)):
            item.setTextAlignment(Qt.AlignCenter)
            item.setFont(font)
            table.setItem(r, c, item)

    return table


# 1 把需要被更新的数据委托给子线程，由子线程完成游戏逻辑
class GameLoop(QObject):
    pass


# 2 测试子程序，临时验证用
class Tester(QObject):
    pass


# 3 游戏主界面
class MainGameGUI(QWidget):
    def __init__(self, game_loop, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.WN = CONST.WORLD_NUMBER
        self.WS = CONST.WORLD_SQUARE_SIZE
        self.ZN = CONST.ZONING_NUMBER
        self.ZS = CONST.ZONING_SQUARE_SIZE

        # 主世界地块列表
        self.WORLD_LIST = []
        # 区划列表
        self.ZONING_LIST = []
        # 备选列表
        self.WAIT_SELECT_LIST = []
        # 资源列表
        self.RESOURCE_LIST = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        # 综合实力列表
        self.POWER_LIST = [0, 0, 0]
        # 科研项目列表
        self.TECHNOLOGY_LABELS = []
        # 科研点转化比例列表, Default = 3:3:4
        self.TECHNOLOGY_RATES = [3, 3, 4]
        # 选择按钮列表, 三个按钮对应触发三个科技的备选列表
        self.TECHNOLOGY_TRANSFORMS = []
        # 详细信息
        self.DETAIL_TEXT = "Empty text"
        # 委托给外部对象
        self.COMMISSION = None
        # wait select list
        self.WAIT_SELECT_WIDGET = None

        # 主世界更新器
        self.WORLD_UPDATER = None
        # 区划更新器
        self.ZONING_UPDATER = None
        # 备选列表更新器
        self.WAITLIST_UPDATER = None
        # 资源面板更新器
        self.RESOURCE_PANEL_UPDATER = None
        # 综合实力面板更新器
        self.POWER_PANEL_UPDATER = None
        # 科研面板更新器
        self.TECHNOLOGY_UPDATER = None
        # 详情面板更新器
        self.DETAIL_PANEL_UPDATER = None

        self.set_ui()
        self.show()

    def clear(self):
        self.DETAIL_TEXT = "Empty text"
        self.WAIT_SELECT_LIST = []
        self.update()

    # 2 绘制主界面
    def set_ui(self):
        width = CONST.WINDOW_WIDTH + 1
        height = CONST.WINDOW_HEIGHT + 1

        self.resize(width, height)
        self.setFixedSize(width, height)
        self.setWindowFlags(Qt.WindowMaximizeButtonHint | Qt.MSWindowsFixedSizeDialogHint)
        self.setWindowTitle(CONST.WINDOW_TITLE)

        self.init_world()
        self.init_zoning()
        self.init_wait_select_list()

        self.draw_resource_panel()
        self.draw_power_panel()
        self.draw_wait_select_panel()
        self.draw_wait_select_options()

    def draw_world(self, painter: QPainter):
        for i in range(CONST.WORLD_NUMBER + 1):
            temp = CONST.WORLD_POSITION_START + i * self.WS
            painter.drawLine(temp, CONST.WORLD_POSITION_START, temp, CONST.WORLD_POSITION_END)
            painter.drawLine(CONST.WORLD_POSITION_START, temp, CONST.WORLD_POSITION_END, temp)

        for rect, text in self.WORLD_LIST:
            text = str(text) if text else ''
            painter.drawText(rect, Qt.AlignCenter, text)

    def draw_zoning(self, painter: QPainter):
        for i in range(CONST.ZONING_NUMBER + 1):
            temp_x = CONST.ZONING_POSITION_START_X + i * self.ZS
            temp_y = CONST.ZONING_POSITION_START_Y + i * self.ZS
            painter.drawLine(temp_x, CONST.ZONING_POSITION_START_Y, temp_x, CONST.ZONING_POSITION_END_Y)
            painter.drawLine(CONST.ZONING_POSITION_START_X, temp_y, CONST.ZONING_POSITION_END_X, temp_y)

        for rect, text in self.ZONING_LIST:
            text = str(text) if text else ''
            painter.drawText(rect, Qt.AlignCenter, text)

    def draw_resource_panel(self):
        table = generate_table(self, 5, 3, 48, 26)
        table.setGeometry(850, 1, 148, 135)
        for row in range(5):
            table.item(row, 0).setText(CONST.RESOURCE_PANELS[row])
            table.item(row, 1).setText(display_number(self.RESOURCE_LIST[row][0]))

            n = self.RESOURCE_LIST[row][1]
            neg = '+' if n >= 0 else '-'
            table.item(row, 2).setText(neg + display_number(abs(n)))

    def draw_power_panel(self):
        table = generate_table(self, 3, 2, 73, 36)
        table.setGeometry(850, 131, 148, 110)
        for row in range(3):
            table.item(row, 0).setText(CONST.POWER_PANELS[row])

            n = self.POWER_LIST[row]
            table.item(row, 1).setText('0' if n <= 0 else display_number(n))

    def draw_wait_select_panel(self):
        self.WAIT_SELECT_WIDGET = QListWidget(self)
        self.WAIT_SELECT_WIDGET.setGeometry(605, 245, 243, 350)

        self.WAIT_SELECT_WIDGET.setStyleSheet("QListWidget{border:1px solid black; color:black; }"
                                              "QListWidget::Item{padding-top:0px; padding-bottom:4px; }"
                                              )
        self.WAIT_SELECT_WIDGET.setSelectionMode(QAbstractItemView.NoSelection)

    def draw_wait_select_options(self):
        for item in self.WAIT_SELECT_LIST:
            option_item = QListWidgetItem()
            option_item.setSizeHint(QSize(200, 120))

            widget = get_wait_item_widget(*item)
            self.WAIT_SELECT_WIDGET.addItem(option_item)
            self.WAIT_SELECT_WIDGET.setItemWidget(option_item, widget)

    # 3 任务委托
    def init_world(self):
        for i in range(self.WN * self.WN):
            x, y = divmod(i, self.WN)

            x1 = CONST.WORLD_POSITION_START + x * self.WS
            y1 = CONST.WORLD_POSITION_START + y * self.WS

            rect = QRect(x1, y1, self.WS, self.WS)
            self.WORLD_LIST.append((rect, 0))

    def init_zoning(self):
        for i in range(self.ZN * self.ZN):
            x, y = divmod(i, self.ZN)

            x1 = CONST.ZONING_POSITION_START_X + x * self.ZS
            y1 = CONST.ZONING_POSITION_START_Y + y * self.ZS

            rect = QRect(x1, y1, self.ZS, self.ZS)
            self.ZONING_LIST.append((rect, 0))

    def init_wait_select_list(self):
        opts = '灵能理论', 30000, ['帝国所有人口消耗 -20%', '帝国所有人口效率 +50%', '军队战斗力 +100%']
        self.WAIT_SELECT_LIST = [opts for _ in range(30)]

    # 4 事件重载
    def paintEvent(self, QPaintEvent):
        p = QPainter()
        p.begin(self)
        self.draw_world(p)
        self.draw_zoning(p)
        p.end()

    # Other


if __name__ == '__main__':
    app = QApplication(sys.argv)

    example = MainGameGUI(None)

    sys.exit(app.exec_())
