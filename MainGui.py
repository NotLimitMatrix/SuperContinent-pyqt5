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
    QTextBrowser,
)
from PyQt5.QtCore import (
    QObject,
    pyqtSignal,
    Qt,
    QRect,
    QSize,
    QThread,
)
from PyQt5.QtGui import (
    QPainter,
    QFont,
)

from static import *


def from_xy_to_position(x, y, size, lt_x, lt_y):
    return lt_x + x * size, lt_y + y * size


def from_index_to_positioin(index, n, size, lt_x, lt_y):
    # lt_x : left_top_x
    # lt_y : left_top_y
    x, y = divmod(index, n)
    return from_xy_to_position(x, y, size, lt_x, lt_y)


def get_wait_item_widget(name, cost, informations):
    name_label = QLabel(name)
    cost_label = QLabel(str(cost))
    line_label = QLabel("----------------------")

    if len(informations) > 3:
        quit(0)
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
    updater = pyqtSignal(dict)

    def __init__(self, main_process, *args, **kwargs):
        self.main_process = main_process
        super().__init__(*args, **kwargs)

    def run(self):
        while True:
            content = self.main_process.display()
            self.updater.emit(content)
            time.sleep(CONST.TIME_FLOW)


# 2 测试子程序，临时验证用
class Tester(QObject):
    pass


# 3 游戏主界面
class MainGameGUI(QWidget):
    def __init__(self, game_loop, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title = CONST.WINDOW_TITLE

        self.WN = CONST.WORLD_NUMBER
        self.WS = CONST.WORLD_SQUARE_SIZE
        self.ZN = CONST.ZONING_NUMBER
        self.ZS = CONST.ZONING_SQUARE_SIZE

        self.TIME_FLOW = 0

        # 主世界地块列表
        self.WORLD_LIST = []
        # 区划列表
        self.ZONING_LIST = []
        # 备选列表
        self.WAIT_SELECT_LIST = []
        # 资源列表
        self.RESOURCE_LIST = [('0', '0')] * 5
        # 综合实力列表
        self.POWER_LIST = ['0'] * 3
        # 科研项目列表
        self.RESEARCH_LABELS = []
        # 科研点转化比例列表, Default = 3:3:4
        self.TECHNOLOGY_RATES = [3, 3, 4]
        # 选择按钮列表, 三个按钮对应触发三个科技的备选列表
        self.TECHNOLOGY_TRANSFORMS = []
        # 详细信息
        self.DETAIL_TEXT = "Empty text"
        # 委托给外部对象
        self.COMMISSION = None
        self.GAME_LOOP = game_loop
        # wait select list
        self.WAIT_SELECT_WIDGET = None

        self.GUI_RESOURCE_PANEL = None
        self.GUI_POWER_PANEL = None
        self.GUI_RATE_BUTTON_LIST = list()
        self.GUI_TRANSFORM_BUTTON_LIST = list()
        self.GUI_DETAIL_TEXT = None

        self.set_ui()
        self.init_game_loop()

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
        self.setWindowTitle(self.title)

        self.init_world()
        self.init_zoning()
        self.init_transform_button()

        self.init_resource_panel()
        self.draw_resource_panel()

        self.init_power_panel()
        self.draw_power_panel()

        self.init_wait_select_list()
        self.draw_wait_select_panel()
        self.draw_wait_select_options()

        self.init_research_panel()
        self.draw_research_panel()

        self.init_rate_button()
        self.draw_rate_button()

        self.init_detail_text()
        self.draw_detail_text()

    def draw_world(self, painter: QPainter):
        for i in range(self.WN):
            for j in range(self.WN):
                x, y = from_xy_to_position(i, j, self.WS, CONST.WORLD_POSITION_START, CONST.WORLD_POSITION_START)
                painter.drawRect(x, y, self.WS, self.WS)
        # for rect, text in self.WORLD_LIST:
        #     text = str(text) if text else ''
        #     painter.drawText(rect, Qt.AlignCenter, text)

    def draw_zoning(self, painter: QPainter):
        for i in range(self.ZN):
            for j in range(self.ZN):
                x, y = from_xy_to_position(i, j, self.ZS, CONST.ZONING_POSITION_START_X, CONST.ZONING_POSITION_START_Y)
                painter.drawRect(x, y, self.ZS, self.ZS)

        # for rect, text in self.ZONING_LIST:
        #     text = str(text) if text else ''
        #     painter.drawText(rect, Qt.AlignCenter, text)

    def init_resource_panel(self):
        table = generate_table(self, 5, 3, 48, 26)
        table.setGeometry(CONST.RESOURCE_PANEL_START_X, CONST.RESOURCE_PANEL_START_Y,
                          CONST.RESOURCE_PANEL_WIDTh, CONST.RESOURCE_PANEL_HEIGHT)

        self.GUI_RESOURCE_PANEL = table

    def draw_resource_panel(self):
        for row in range(5):
            self.GUI_RESOURCE_PANEL.item(row, 0).setText(CONST.RESOURCE_PANELS[row])
            self.GUI_RESOURCE_PANEL.item(row, 1).setText(self.RESOURCE_LIST[row][0])
            self.GUI_RESOURCE_PANEL.item(row, 2).setText(self.RESOURCE_LIST[row][1])
            # self.GUI_RESOURCE_PANEL.item(row, 1).setText(display_number(self.RESOURCE_LIST[row][0]))
            #
            # n = self.RESOURCE_LIST[row][1]
            # neg = '+' if n >= 0 else '-'
            # self.GUI_RESOURCE_PANEL.item(row, 2).setText(neg + display_number(abs(n)))

    def init_power_panel(self):
        table = generate_table(self, 3, 2, 73, 36)
        table.setGeometry(CONST.POWER_PANEL_START_X, CONST.POWER_PANEL_START_Y,
                          CONST.POWER_PANEL_WIDTH, CONST.POWER_PANEL_HEIGHT)

        self.GUI_POWER_PANEL = table

    def draw_power_panel(self):
        for row in range(3):
            self.GUI_POWER_PANEL.item(row, 0).setText(CONST.POWER_PANELS[row])
            self.GUI_POWER_PANEL.item(row, 1).setText(self.POWER_LIST[row])

    def draw_wait_select_panel(self):
        self.WAIT_SELECT_WIDGET = QListWidget(self)
        self.WAIT_SELECT_WIDGET.setGeometry(CONST.WAIT_PANEL_START_X, CONST.WAIT_PANEL_START_Y,
                                            CONST.WAIT_PANEL_WIDTH, CONST.WAIT_PANEL_HEIGHT)

        self.WAIT_SELECT_WIDGET.setStyleSheet("QListWidget{border:1px solid black; color:black; }"
                                              "QListWidget::Item{padding-top:0px; padding-bottom:4px; }"
                                              )
        self.WAIT_SELECT_WIDGET.setSelectionMode(QAbstractItemView.NoSelection)

    def draw_wait_select_options(self):
        self.WAIT_SELECT_WIDGET.clear()
        if self.WAIT_SELECT_LIST is None:
            return

        for item in self.WAIT_SELECT_LIST:
            option_item = QListWidgetItem()
            option_item.setSizeHint(QSize(200, 120))
            widget = get_wait_item_widget(*item)
            self.WAIT_SELECT_WIDGET.addItem(option_item)
            self.WAIT_SELECT_WIDGET.setItemWidget(option_item, widget)

    def draw_research_panel(self):
        not_empty = bool(self.RESEARCH_LABELS)

        for i in range(3):
            label = QLabel(self)
            label.setGeometry(CONST.RESEARCH_LABEL_START_X, CONST.RESEARCH_LABEL_START_Y + i * 20,
                              100, 18)
            label.setStyleSheet(CONST.RESEARCE_LABEL_STYLE)
            if not_empty:
                t = self.RESEARCH_LABELS[i]
                label.setText(f"{t[0]} : {t[1]}%")
            else:
                label.setText('没有研究')

    def init_rate_button(self):
        for i in range(3):
            rate_button = QPushButton(self)
            rate_button.setGeometry(CONST.RESEARCH_RATE_BUTTON_START_X, CONST.RESEARCH_RATE_BUTTON_START_Y + i * 20, 30,
                                    30)
            rate_button.setText('')
            self.GUI_RATE_BUTTON_LIST.append(rate_button)

    def draw_rate_button(self):
        for i in range(3):
            btn = self.GUI_RATE_BUTTON_LIST[i]
            btn.setText(str(self.TECHNOLOGY_RATES[i]))

    def init_transform_button(self):
        for i in range(3):
            transform_button = QPushButton(self)
            transform_button.setGeometry(CONST.RESEARCH_TRANSFORM_START_X, CONST.RESEARCH_TRANSFORM_START_Y + i * 20,
                                         30, 30)
            transform_button.setText('T')
            self.GUI_TRANSFORM_BUTTON_LIST.append(transform_button)

    def draw_detail_text(self):
        if self.DETAIL_TEXT is None:
            self.GUI_DETAIL_TEXT.setText('暂无消息')
        else:
            self.GUI_DETAIL_TEXT.setText(self.DETAIL_TEXT)

    def draw_time_flow(self):
        years, o = divmod(self.TIME_FLOW, 360)
        months, days = divmod(o, 30)

        self.setWindowTitle(f"{self.title} 【TIME: {years}-{months}-{days}】")

    # 3 任务委托
    def init_world(self):
        pass

    def init_zoning(self):
        pass

    def init_wait_select_list(self):
        self.WAIT_SELECT_LIST = None

    def init_research_panel(self):
        self.RESEARCH_LABELS = None

    def init_detail_text(self):
        # 为保证显示效果，单行长度不超过20
        textBrowser = QTextBrowser(self)
        textBrowser.setGeometry(CONST.DETAIL_START_X, CONST.DETAIL_START_Y,
                                CONST.DETAIL_WIDTH, CONST.DETAIL_HEIGHT)
        font = QFont()
        font.setPixelSize(12)

        textBrowser.setFont(font)
        self.GUI_DETAIL_TEXT = textBrowser
        self.DETAIL_TEXT = None

    # 4 事件重载
    def paintEvent(self, QPaintEvent):
        p = QPainter()
        p.begin(self)
        self.draw_world(p)
        self.draw_zoning(p)
        p.end()

    # 更新时间轴
    def update_game(self, content: dict):
        self.TIME_FLOW += content.get('time_flow')
        self.draw_time_flow()

        self.RESOURCE_LIST = content.get('resources_list')[:]
        self.draw_resource_panel()

        self.POWER_LIST = content.get('power_list')[:]
        self.draw_power_panel()

        wsl = content['wait_select_list']['options']
        if wsl == self.WAIT_SELECT_LIST:
            pass
        else:
            self.WAIT_SELECT_LIST = wsl[:]
            self.draw_wait_select_options()

        detail_text = content.get('detail_text')
        if detail_text == self.DETAIL_TEXT: \
                pass
        else:
            self.DETAIL_TEXT = detail_text
            self.draw_detail_text()

        self.update()

    def init_game_loop(self):
        self.COMMISSION = GameLoop(self.GAME_LOOP)
        self.COMMISSION.updater.connect(self.update_game)
        self.thread = QThread()
        self.COMMISSION.moveToThread(self.thread)
        self.thread.started.connect(self.COMMISSION.run)
        self.thread.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    example = MainGameGUI(None)

    sys.exit(app.exec_())
