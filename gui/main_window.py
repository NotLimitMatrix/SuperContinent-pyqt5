from pprint import pprint

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPainter
from PyQt5 import QtGui

from reference.gui import SIZE, POSITION, GUI_KEY, NUMBER
from reference import dictionary
from reference import functions
from gui.gui_world import WorldGUI
from gui.gui_zoning import ZoningGUI
from gui.gui_panel import PanelGUI
from gui.gui_technology import TechnologyGUI
from gui.gui_text_browser import TextBrowserGUI
from gui.gui_select import SelectGUI
from gui.gui_filter import FilterGUI

from unit.block import Block

test_message = """
地块: 01
坐标: 1,2
环境: 恶劣
资源:
    食物: +2
    矿物: +4
    能量: -1
"""

MAIN_MEMORY = {
    GUI_KEY.WORLD: [
        Block(i, *functions.ident_to_row_col(i, NUMBER.WORLD_NUMBER), SIZE.WORLD_WIDTH // NUMBER.WORLD_NUMBER)
        for i in range(NUMBER.WORLD_NUMBER * NUMBER.WORLD_NUMBER)
    ],
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
        dictionary.MILITARY: ('蓝色激光', 36987, 4321),
        dictionary.BEYOND: ('进化破译', 9568, 10248),
        'more_point': 0
    },
    GUI_KEY.SELECT: [i for i in range(6)],
    GUI_KEY.TEXT_BROWSER: test_message
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
                                      width=SIZE.SELECT_WIDTH, height=SIZE.SELECT_HEIGHT),
            GUI_KEY.FILTER: FilterGUI(top=POSITION.FILTER_TOP, left=POSITION.FILTER_LEFT,
                                      width=SIZE.FILTER_WIDTH, height=SIZE.FILTER_HEIGHT)
        }

        self.memory = MAIN_MEMORY
        self.update_data()

        self.resize(SIZE.WINDOW_WIDTH + 1, SIZE.WINDOW_HEIGHT + 1)
        self.setFixedSize(SIZE.WINDOW_WIDTH + 1, SIZE.WINDOW_HEIGHT + 1)
        self.setWindowTitle('Super Continent')

        self.show()

    def update_data(self):
        d = dict()
        # 根据memory更新界面
        for key, value in self.memory.items():
            response = self.components[key].update(value)
            if response is not None:
                d[key] = response

        # 根据界面变动返回结果更新memory
        self.memory.update(d)
        pprint(self.memory)
        self.update()

    # 绘制界面
    def draw_window(self, painter: QPainter):
        for component in self.components.values():
            component.draw(painter)

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

    # def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
    #     c_name, component = self.choose_component(event)
    #     if c_name == GUI_KEY.WORLD:
    #         self.update_data()
