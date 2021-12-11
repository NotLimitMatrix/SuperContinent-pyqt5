import random

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QMainWindow, QAction, qApp

from gui.gui_filter import FilterGUI
from gui.gui_panel import PanelGUI
from gui.gui_select import SelectGUI
from gui.gui_technology import TechnologyGUI
from gui.gui_text_browser import TextBrowserGUI
from gui.gui_world import WorldGUI
from gui.gui_zoning import ZoningGUI
from gui.gui_console import ConsoleGUI
from gui.console import ConsoleWidget
from player.player import Player
from reference import functions
from reference.gui import SIZE, POSITION, GUI_KEY
from unit.block import Block
from unit.memory import Memory


class MainGameGUI(QMainWindow):
    def __init__(self, player: Player, *args, **kwargs):
        self.player = player

        super(MainGameGUI, self).__init__(*args, **kwargs)

        self.console = None

        self.components = {
            GUI_KEY.WORLD: WorldGUI(top=POSITION.WORLD_TOP, left=POSITION.WORLD_LEFT,
                                    width=SIZE.WORLD_WIDTH, height=SIZE.WORLD_HEIGHT, parent=self),
            GUI_KEY.ZONING: ZoningGUI(top=POSITION.ZONING_TOP, left=POSITION.ZONING_LEFT,
                                      width=SIZE.ZONING_WIDTH, height=SIZE.ZONING_HEIGHT, parent=self),
            GUI_KEY.PANEL: PanelGUI(top=POSITION.PANEL_TOP, left=POSITION.PANEL_LEFT,
                                    width=SIZE.PANEL_WIDTH, height=SIZE.PANEL_HEIGHT, parent=self),
            GUI_KEY.TECHNOLOGY: TechnologyGUI(top=POSITION.TECHNOLOGY_TOP, left=POSITION.TECHNOLOGY_LEFT,
                                              width=SIZE.TECHNOLOGY_WIDTH, height=SIZE.TECHNOLOGY_HEIGHT, parent=self),
            GUI_KEY.TEXT_BROWSER: TextBrowserGUI(top=POSITION.TEXT_BROWSER_TOP, left=POSITION.TEXT_BROWSER_LEFT,
                                                 width=SIZE.TEXT_BROWSER_WIDTH, height=SIZE.TEXT_BROWSER_HEIGHT,
                                                 parent=self),
            GUI_KEY.SELECT: SelectGUI(top=POSITION.SELECT_TOP, left=POSITION.SELECT_LEFT,
                                      width=SIZE.SELECT_WIDTH, height=SIZE.SELECT_HEIGHT, parent=self),
            GUI_KEY.FILTER: FilterGUI(top=POSITION.FILTER_TOP, left=POSITION.FILTER_LEFT,
                                      width=SIZE.FILTER_WIDTH, height=SIZE.FILTER_HEIGHT, parent=self),
            GUI_KEY.TOOL: ConsoleGUI(top=POSITION.TOOL_BAR_TOP, left=POSITION.TOOL_BAR_LEFT,
                                     width=SIZE.TOOL_BAR_WIDTH, height=SIZE.TOOL_BAR_HEIGHT, parent=self)
        }

        self.memory = Memory()
        self.update_data()

        self.player.init_player(self.components[GUI_KEY.WORLD].world_list)

        self.resize(SIZE.WINDOW_WIDTH + 1, SIZE.WINDOW_HEIGHT + 1)
        self.setFixedSize(SIZE.WINDOW_WIDTH + 1, SIZE.WINDOW_HEIGHT + 1)
        self.setWindowTitle(f'Super Continent [{functions.game_time_to_date(0)}]')

        self.show()

    def update_data(self):
        # 根据memory更新界面
        for key, value in self.memory.dump()['GUI'].items():
            if key == GUI_KEY.OTHER:
                continue

            self.components[key].update(value)

        self.update()

    # 绘制界面
    def draw_window(self, painter: QPainter):
        self.components[GUI_KEY.WORLD].draw(painter, self.memory.filter_type, self.player.color)
        self.components[GUI_KEY.ZONING].draw(painter)
        self.components[GUI_KEY.PANEL].draw(painter)
        self.components[GUI_KEY.TECHNOLOGY].draw(painter)
        self.components[GUI_KEY.TEXT_BROWSER].draw(painter)
        self.components[GUI_KEY.SELECT].draw(painter)
        self.components[GUI_KEY.FILTER].draw(painter)
        self.components[GUI_KEY.TOOL].draw(painter)
        # for component in self.components.values():
        #     component.draw(painter)

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        p = QPainter()
        p.begin(self)
        self.draw_window(p)
        p.end()

    def choose_component(self, event):
        for c_name, item_component in self.components.items():
            if item_component.in_this(event):
                return c_name, item_component
        return None, None

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        c_name, component = self.choose_component(event)
        if c_name is None:
            return

        click = event.buttons()

        if click == Qt.LeftButton:
            match c_name:
                case GUI_KEY.WORLD:
                    block: Block = component.mouse_choose_item(event)
                    if block.attribute.display:
                        self.memory.update_block(block.ident)
                        self.memory.msg = block.display()
                    else:
                        self.memory.msg = "该地块不可见"
                case GUI_KEY.TEXT_BROWSER:
                    self.memory.msg = 'In TextBrowser'
                case GUI_KEY.FILTER:
                    filter_item = component.mouse_choose_item(event)
                    self.memory.filter_type = filter_item.name
                    self.memory.msg = filter_item.display()

        if click == Qt.RightButton:
            self.memory.msg = f"右键:\n{event.pos().x()}, {event.pos().y()}\n"
        self.update_data()
