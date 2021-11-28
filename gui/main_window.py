from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPainter
from PyQt5 import QtGui

from reference.gui import SIZE, POSITION, GUI_KEY
from reference import dictionary

from gui.gui_world import WorldGUI
from gui.gui_zoning import ZoningGUI
from gui.gui_panel import PanelGUI
from gui.gui_technology import TechnologyGUI
from gui.gui_text_browser import TextBrowserGUI
from gui.gui_select import SelectGUI

MAIN_MEMORY = {
    GUI_KEY.WORLD: [i for i in range(100)],
    GUI_KEY.ZONING: [i for i in range(36)],
    GUI_KEY.PANEL: {
        dictionary.FOOD: (0, 10),
        dictionary.MINERAL: (0, 10),
        dictionary.ENERGY: (0, 10),
        dictionary.COMMODITY: (0, 10),
        dictionary.ALLOY: (0, 10),
        dictionary.POPULATION: 10,
        dictionary.ECONOMY: 10,
        dictionary.MILITARY: 10,
        dictionary.TECHNOLOGY: 10
    },
    GUI_KEY.TECHNOLOGY: {
        dictionary.ECONOMY: ('矿产探测', 2301, 5689),
        dictionary.MILITARY: ('蓝色激光', 3569, 4321),
        dictionary.BEYOND: ('进化破译', 9568, 10248)
    },
    GUI_KEY.SELECT: [i for i in range(6)],
    'msg': None
}


class MainGameGUI(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainGameGUI, self).__init__(*args, **kwargs)

        self.components = {
            GUI_KEY.WORLD: WorldGUI(top=POSITION.WORLD_TOP, left=POSITION.WORLD_LEFT,
                                    width=SIZE.WORLD_WIDTH, height=SIZE.WORLD_HEIGHT),
            GUI_KEY.ZONING: ZoningGUI(top=POSITION.ZONING_TOP, left=POSITION.ZONING_LEFT,
                                      width=SIZE.ZONING_WIDTH, height=SIZE.ZONING_HEIGHT),
            GUI_KEY.PANEL: PanelGUI(top=POSITION.PANEL_TOP, left=POSITION.PANEL_LEFT,
                                    width=SIZE.PANEL_WIDTH, height=SIZE.PANEL_HEIGHT),
            GUI_KEY.TECHNOLOGY: TechnologyGUI(top=POSITION.TECHNOLOGY_TOP, left=POSITION.TECHNOLOGY_LEFT,
                                              width=SIZE.TECHNOLOGY_WIDTH, height=SIZE.TECHNOLOGY_HEIGHT),
            GUI_KEY.TEXT_BROWSER: TextBrowserGUI(top=POSITION.TEXT_BROWSER_TOP, left=POSITION.TEXT_BROWSER_LEFT,
                                                 width=SIZE.TEXT_BROWSER_WIDTH, height=SIZE.TEXT_BROWSER_HEIGHT),
            GUI_KEY.SELECT: SelectGUI(top=POSITION.SELECT_TOP, left=POSITION.SELECT_LEFT,
                                      width=SIZE.SELECT_WIDTH, height=SIZE.SELECT_HEIGHT)
        }

        self.memory = MAIN_MEMORY
        self.update_data()

        self.resize(SIZE.WINDOW_WIDTH + 1, SIZE.WINDOW_HEIGHT + 1)
        self.setFixedSize(SIZE.WINDOW_WIDTH + 1, SIZE.WINDOW_HEIGHT + 1)
        self.setWindowTitle('Super Continent')

        self.show()

    def update_data(self):
        # for cname, values in self.memory.items():
        #     print(cname)
        #     component = self.components[cname]
        #     component.update(values)
        self.components[GUI_KEY.TECHNOLOGY].update(self.memory[GUI_KEY.TECHNOLOGY])

        self.update()

    # 绘制界面
    def draw_window(self, painter: QPainter):
        for component in self.components.values():
            component.draw_component(painter)

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        p = QPainter()
        p.begin(self)
        self.draw_window(p)
        p.end()

    def choose_component(self, event):
        for c_name, item_component in self.components:
            if item_component.in_this(event):
                return c_name, item_component
        return None

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        c_name, component = self.choose_component(event)
        if c_name == GUI_KEY.WORLD:
            self.update_data()
