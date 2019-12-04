from GUI import (
    QMainWindow,
    Qt,
    QThread,
    QPainter,
    CONST,
)

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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
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

        self.TIMER = Timer(self)
        self.GUI_WORLD = World(self.WS, self.WN)
        self.GUI_ZONING = Zoning(self.ZS, self.ZN)
        self.GUI_WAIT_SELECT = WaitSelect(self)
        self.GUI_RESOURCE_PANEL = GuiResourcePanel(self)
        self.GUI_POWER_PANEL = GuiPowerPanel(self)
        self.GUI_RESEARCH_PAENL = ResearcherPanel(self)
        self.GUI_DETAIL_TEXT = DetailText(self)

        self.show()

    def update_game(self, content):
        self.TIMER.update(content.get(INTERFACE.TIME_FLOW))
        self.GUI_RESOURCE_PANEL.update(content.get(INTERFACE.RESOURCES))
        self.GUI_POWER_PANEL.update(content.get(INTERFACE.POWERS))
        self.GUI_WAIT_SELECT.update(content[INTERFACE.WAIT_SELECT_ITEMS][INTERFACE.WAIT_ITEMS_OPTIONS])
        self.GUI_RESEARCH_PAENL.update(content.get(INTERFACE.RESEARCHER_ITEMS))
        self.GUI_DETAIL_TEXT.update(content.get(INTERFACE.DETAIL_TEXT))
        self.update()

    def init_GameLoop(self, game_loop):
        self.COMMISSION = GameLoop(game_loop)
        self.COMMISSION.updater.connect(self.update_game)
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
