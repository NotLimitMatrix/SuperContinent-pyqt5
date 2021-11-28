from PyQt5.QtWidgets import (
    QAbstractItemView,
    QListWidget,
    QListWidgetItem,
    QTextBrowser,
    QAction,
    QMainWindow,
    qApp,
)
from PyQt5.QtCore import (
    QObject,
    pyqtSignal,
    Qt,
    QSize,
    QThread,
)
from PyQt5.QtGui import (
    QPainter,
    QFont,
)

from Recycle.static import *
from Recycle.ItemWidget import TechnologyItemWidget
from Recycle.SubGui import GenerateTable, OneResearchPanel


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


class MainGameGUI(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.WN = CONST.WORLD_NUMBER
        self.WS = CONST.WORLD_SQUARE_SIZE
        self.ZN = CONST.ZONING_NUMBER
        self.ZS = CONST.ZONING_SQUARE_SIZE
        self.title = CONST.WINDOW_TITLE

        self.COMMISSION = None

        # 时间进度
        self.TIME_FLOW = 0

        # 主世界和区划
        self.WORLD_LIST = []
        self.ZONING_LIST = []

        # 备选列表GUI和Item列表
        self.GUI_WAIT_SELECT = self.init_GUI_WAIT_SELECT()
        self.WAIT_SELECT_ITEMS = []

        # 资源面板GUI和资源信息列表
        self.GUI_RESOURCE_PANEL = self.init_GUI_RESEARCE_PANEL()
        self.RESOURCE_LIST = [['0', '0'], ['0', '0'], ['0', '0'], ['0', '0'], ['0', '0']]

        # 综合实力面板GUI和实力数据列表
        self.GUI_POWER_PANEL = self.init_GUI_POWER_PANEL()
        self.POWER_LIST = ['0', '0', '0']

        # 科研面板GUI和科研信息列表
        self.GUI_RESEARCH_PAENL = self.init_GUI_RESEARCH_PANEL()
        self.RESEARCH_INFO_LIST = {
            KEY.MILITARY: (None, None),
            KEY.CIVIL: (None, None),
            KEY.HYPER: (None, None)
        }

        # 情报GUI和情报内容
        self.GUI_DETAIL_TEXT = self.init_GUI_DETAIL_TEXT()
        self.DETAIL_TEXT = '没有信息'

        self.set_UI()
        self.set_menu_bar()

        self.show()

    def init_GUI_WAIT_SELECT(self):
        wsw = QListWidget(self)
        wsw.setGeometry(CONST.WAIT_PANEL_START_X, CONST.WAIT_PANEL_START_Y,
                        CONST.WAIT_PANEL_WIDTH, CONST.WAIT_PANEL_HEIGHT)
        wsw.setStyleSheet("QListWidget{border:1px solid black; color:black; }"
                          "QListWidget::Item{padding-top:0px; padding-bottom:4px; }")
        wsw.setSelectionMode(QAbstractItemView.NoSelection)
        return wsw

    def init_GUI_RESEARCE_PANEL(self):
        table = GenerateTable(self, 5, 3, 48, 26)
        table.setGeometry(CONST.RESOURCE_PANEL_START_X, CONST.RESOURCE_PANEL_START_Y,
                          CONST.RESOURCE_PANEL_WIDTh, CONST.RESOURCE_PANEL_HEIGHT)

        return table

    def init_GUI_POWER_PANEL(self):
        table = GenerateTable(self, 3, 2, 73, 36)
        table.setGeometry(CONST.POWER_PANEL_START_X, CONST.POWER_PANEL_START_Y,
                          CONST.POWER_PANEL_WIDTH, CONST.POWER_PANEL_HEIGHT)

        return table

    def init_GUI_RESEARCH_PANEL(self):
        r_military = OneResearchPanel(self)
        r_military.init_label(CONST.RESEARCH_LABEL_START_X, CONST.RESEARCH_LABEL_START_Y)
        r_military.init_rate_button(CONST.RESEARCH_RATE_BUTTON_START_X, CONST.RESEARCH_RATE_BUTTON_START_Y)
        r_military.init_transform_button(CONST.RESEARCH_TRANSFORM_START_X, CONST.RESEARCH_TRANSFORM_START_Y)

        r_civil = OneResearchPanel(self)
        r_civil.init_label(CONST.RESEARCH_LABEL_START_X, CONST.RESEARCH_LABEL_START_Y + 20)
        r_civil.init_rate_button(CONST.RESEARCH_RATE_BUTTON_START_X, CONST.RESEARCH_RATE_BUTTON_START_Y + 20)
        r_civil.init_transform_button(CONST.RESEARCH_TRANSFORM_START_X, CONST.RESEARCH_TRANSFORM_START_Y + 20)

        r_beyond = OneResearchPanel(self)
        r_beyond.init_label(CONST.RESEARCH_LABEL_START_X, CONST.RESEARCH_LABEL_START_Y + 40)
        r_beyond.init_rate_button(CONST.RESEARCH_RATE_BUTTON_START_X, CONST.RESEARCH_RATE_BUTTON_START_Y + 40)
        r_beyond.init_transform_button(CONST.RESEARCH_TRANSFORM_START_X, CONST.RESEARCH_TRANSFORM_START_Y + 40)

        return {
            KEY.MILITARY: r_military,
            KEY.CIVIL: r_civil,
            KEY.HYPER: r_beyond
        }

    def init_GUI_DETAIL_TEXT(self):
        textBrowser = QTextBrowser(self)
        textBrowser.setGeometry(CONST.DETAIL_START_X, CONST.DETAIL_START_Y,
                                CONST.DETAIL_WIDTH, CONST.DETAIL_HEIGHT)
        font = QFont()
        font.setPixelSize(12)

        textBrowser.setFont(font)
        return textBrowser

    def init_GameLoop(self, game_loop):
        self.COMMISSION = GameLoop(game_loop)
        self.COMMISSION.updater.connect(self.update_game)
        self.thread = QThread()
        self.COMMISSION.moveToThread(self.thread)
        self.thread.started.connect(self.COMMISSION.run)
        self.thread.start()

    def update_time(self):
        years, o = divmod(self.TIME_FLOW, 360)
        months, days = divmod(o, 30)
        self.setWindowTitle(f"{self.title} 【TIME: {years}-{months}-{days}】")

    def update_WORLD(self, painter: QPainter):
        for i in range(self.WN):
            for j in range(self.WN):
                x, y = from_xy_to_position(i, j, self.WS, CONST.WORLD_POSITION_START, CONST.WORLD_POSITION_START)
                painter.drawRect(x, y, self.WS, self.WS)

    def update_ZONING(self, painter: QPainter):
        for i in range(self.ZN):
            for j in range(self.ZN):
                x, y = from_xy_to_position(i, j, self.ZS, CONST.ZONING_POSITION_START_X, CONST.ZONING_POSITION_START_Y)
                painter.drawRect(x, y, self.ZS, self.ZS)

    def update_GUI_WAIT_SELECT(self):
        self.GUI_WAIT_SELECT.clear()
        if self.WAIT_SELECT_ITEMS is None:
            return

        for item in self.WAIT_SELECT_ITEMS:
            option_item = QListWidgetItem()
            option_item.setSizeHint(QSize(200, 120))

            W = TechnologyItemWidget(t=KEY.TECHNOLOGY, datas=item).to_widget()
            self.GUI_WAIT_SELECT.addItem(option_item)
            self.GUI_WAIT_SELECT.setItemWidget(option_item, W)

    def update_GUI_RESOURCE_PANEL(self):
        for row in range(5):
            stroage, daily = self.RESOURCE_LIST[row]
            self.GUI_RESOURCE_PANEL.item(row, 0).setText(CONST.RESOURCE_PANELS[row])
            self.GUI_RESOURCE_PANEL.item(row, 1).setText(stroage)
            self.GUI_RESOURCE_PANEL.item(row, 2).setText(daily)

    def update_GUI_POWER_PANEL(self):
        for row in range(3):
            self.GUI_POWER_PANEL.item(row, 0).setText(CONST.POWER_PANELS[row])
            self.GUI_POWER_PANEL.item(row, 1).setText(self.POWER_LIST[row])

    def update_GUI_RESEARCH_PANEL(self):
        for key in [KEY.MILITARY, KEY.CIVIL, KEY.HYPER]:
            info = self.RESEARCH_INFO_LIST.get(key)
            panel = self.GUI_RESEARCH_PAENL.get(key)
            panel.display(info)

    def update_GUI_DETAIL_TEXT(self):
        if self.DETAIL_TEXT is None:
            self.GUI_DETAIL_TEXT.setText('没有消息')
        else:
            self.GUI_DETAIL_TEXT.setText(self.DETAIL_TEXT)

    def update_game(self, content):
        self.TIME_FLOW += content.get('time_flow')
        self.update_time()

        self.RESOURCE_LIST = content.get('resources_list')[:]
        self.update_GUI_RESOURCE_PANEL()

        self.POWER_LIST = content.get('power_list')[:]
        self.update_GUI_POWER_PANEL()

        wsl = content['wait_select_list']['options']
        if wsl == self.WAIT_SELECT_ITEMS:
            pass
        else:
            self.WAIT_SELECT_ITEMS = wsl[:]
            self.update_GUI_WAIT_SELECT()

        dtt = content['detail_text']
        if dtt == self.DETAIL_TEXT:
            pass
        else:
            self.DETAIL_TEXT = dtt
            self.update_GUI_DETAIL_TEXT()

        self.RESEARCH_INFO_LIST = content.get('research_label_list')
        self.update_GUI_RESEARCH_PANEL()

        self.update()

    def set_menu_bar(self):
        main_menu_bar = self.menuBar()

        exitAct = QAction('退出游戏', self)
        exitAct.triggered.connect(qApp.quit)

        start_game = QAction("开始游戏", self)
        load_data = QAction("载入存档", self)
        export_data = QAction("保存存档", self)
        net_game = QAction("联机对战", self)

        game = main_menu_bar.addMenu('游戏')

        game.addAction(start_game)
        game.addAction(net_game)
        game.addAction(load_data)
        game.addAction(export_data)
        game.addAction(exitAct)

    def set_UI(self):
        width = CONST.WINDOW_WIDTH + 1
        height = CONST.WINDOW_HEIGHT + 1

        self.resize(width, height)
        self.setFixedSize(width, height)
        self.setWindowFlags(Qt.WindowMaximizeButtonHint | Qt.MSWindowsFixedSizeDialogHint)
        self.setWindowTitle(self.title)

    def paintEvent(self, QPaintEvent):
        p = QPainter()
        p.begin(self)
        self.update_WORLD(p)
        self.update_ZONING(p)
        p.end()
