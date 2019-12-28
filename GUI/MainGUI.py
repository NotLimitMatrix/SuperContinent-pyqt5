from GUI import (
    CONST,
    METHOD,
    Static,
    QMainWindow,
    Qt,
    QThread,
    QPainter,
    pyqtSignal,
    QMenu,
    qApp,
)

from Core import COLOR

from GUI.GameLoop import GameLoop
from GUI.GUI_timer import Timer
from GUI.GUI_world import World
from GUI.GUI_zoning import Zoning
from GUI.GUI_wait_select import WaitSelect
from GUI.GUI_resource_panel import GuiResourcePanel
from GUI.GUI_power_panel import GuiPowerPanel
from GUI.GUI_researcher_panel import ResearcherPanel
from GUI.GUI_detail_text import DetailText
from GUI.GUI_menu import Menu
from Core import INTERFACE


class MainGameGUI(QMainWindow):
    SENDER = pyqtSignal(dict)

    def __init__(self, game_loop, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.GAME_LOOP = game_loop
        self.WN = CONST.WORLD_NUMBER
        self.WS = CONST.WORLD_SQUARE_SIZE
        self.ZN = CONST.ZONING_NUMBER
        self.ZS = CONST.ZONING_SQUARE_SIZE
        self.title = CONST.WINDOW_TITLE

        self.resize(CONST.WINDOW_WIDTH + 1, CONST.WINDOW_HEIGHT + 1)
        self.setFixedSize(CONST.WINDOW_WIDTH + 1, CONST.WINDOW_HEIGHT + 1)
        self.setWindowFlags(Qt.WindowMaximizeButtonHint | Qt.MSWindowsFixedSizeDialogHint)
        self.setWindowTitle(self.title)

        self.GUI_MENU = Menu(self)

        self.COMMISSION = None
        self.CONTENT = INTERFACE.MESSAGE_TEMPLATE.copy()

        self.TIMER = Timer(self)
        self.GUI_WORLD = World(self.WS, self.WN)
        self.GUI_ZONING = Zoning(self.ZS, self.ZN)
        self.GUI_WAIT_SELECT = WaitSelect(self)
        self.GUI_RESOURCE_PANEL = GuiResourcePanel(self)
        self.GUI_POWER_PANEL = GuiPowerPanel(self)
        self.GUI_RESEARCH_PAENL = ResearcherPanel(self)
        self.GUI_DETAIL_TEXT = DetailText(self)

        self.init_GameLoop()

        self.show()

        self.GUI_WORLD.block(32).neg_observable()
        self.GUI_WORLD.block(33).neg_observable()
        self.GUI_WORLD.block(34).neg_observable()
        self.GUI_WORLD.block(35).neg_observable()
        self.GUI_WORLD.block(36).neg_observable()

        # Static
        self.Memory = []
        self.Selected = None

    def NewGame(self, wn):
        self.TIMER = Timer(self)
        self.WN = wn
        self.WS = CONST.WORLD_WIDTH // self.WN
        self.GUI_WORLD = World(self.WS, self.WN)

    def self_update(self):
        self.TIMER.update(self.CONTENT.get(INTERFACE.TIME_FLOW))
        self.GUI_RESOURCE_PANEL.update(self.CONTENT.get(INTERFACE.RESOURCES))
        self.GUI_POWER_PANEL.update(self.CONTENT.get(INTERFACE.POWERS))
        self.GUI_WAIT_SELECT.update(self.CONTENT[INTERFACE.WAIT_SELECT_ITEMS][INTERFACE.WAIT_ITEMS_OPTIONS])
        self.GUI_RESEARCH_PAENL.update(self.CONTENT.get(INTERFACE.RESEARCHER_ITEMS))
        self.GUI_DETAIL_TEXT.update(self.CONTENT.get(INTERFACE.DETAIL_TEXT))
        self.update()

    def update_game(self, content):
        self.update_content(content)
        self.self_update()

    def update_content(self, content: dict):
        self.CONTENT = content.copy()

    def init_GameLoop(self):
        self.COMMISSION = GameLoop(self.GAME_LOOP)

        self.COMMISSION.updater.connect(self.update_game)
        self.SENDER.connect(self.COMMISSION.recv)

        self.thread = QThread()
        self.COMMISSION.moveToThread(self.thread)
        self.thread.started.connect(self.COMMISSION.run)
        self.thread.start()

    def paintEvent(self, QPaintEvent):
        p = QPainter()
        p.begin(self)
        self.GUI_WORLD.update(p)
        self.GUI_ZONING.update(p)
        p.end()

    def mousePressEvent(self, event):
        b = event.buttons()

        x = event.pos().x()
        y = event.pos().y()

        for m in self.Memory:
            temp_block = self.GUI_WORLD.block(m)
            temp_block.clear_color()

        # 左键单击
        if b == Qt.LeftButton:
            if METHOD.mouse_int_world(x, y):
                block_id = METHOD.mouse_in_which_block(x, y, self.WS, self.WN)
                block = self.GUI_WORLD.block(block_id)

                ids = block.ids
                if self.Selected:
                    select_ids = self.Selected.ids
                    # points = self.GUI_WORLD.AStar_path(select_ids.x, select_ids.y, ids.x, ids.y)
                    points = self.GUI_WORLD.found_path(self.Selected.ids, ids)
                    self.Memory = METHOD.points_to_indexs(points, self.WN)

                    self.Selected.clear_color()
                    self.Selected = None
                else:
                    points = self.GUI_WORLD.square_from_one_walk(ids.x, ids.y)
                    # points = self.GUI_WORLD.square_from_one_xy(ids.x, ids.y, 1)
                    self.Memory = METHOD.points_to_indexs(points, self.WN)

                for m in self.Memory:
                    temp_block = self.GUI_WORLD.block(m)
                    temp_block.set_color(COLOR.Red)

                self.CONTENT[INTERFACE.DETAIL_TEXT] = block.display()
                self.GUI_ZONING.set_number(block.zoning_number)
        # 右键单击
        if b == Qt.RightButton:
            if self.Selected:
                self.Selected.clear_color()

            if METHOD.mouse_int_world(x, y):
                block_id = METHOD.mouse_in_which_block(x, y, self.WS, self.WN)
                block = self.GUI_WORLD.block(block_id)
                block.set_color(COLOR.White)
                self.Selected = block

        self.self_update()

    # 鼠标右键上下文菜单
    def contextMenuEvent(self, event):
        x = event.pos().x()
        y = event.pos().y()

        if not METHOD.mouse_int_world(x, y) and not METHOD.mouse_in_zoning(x, y):
            cmenu = QMenu(self)
            newAct = cmenu.addAction("新建 10x10游戏")
            opnAct = cmenu.addAction("保存")
            quitAct = cmenu.addAction("退出")
            action = cmenu.exec_(self.mapToGlobal(event.pos()))
            if action == quitAct:
                qApp.quit()
            if action == newAct:
                self.NewGame(10)
