from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QMainWindow

from gui.gui_filter import FilterGUI
from gui.gui_panel import PanelGUI
from gui.gui_select import SelectGUI
from gui.gui_technology import TechnologyGUI
from gui.gui_text_browser import TextBrowserGUI
from gui.gui_world import WorldGUI
from gui.gui_zoning import ZoningGUI
from reference import functions
from reference.gui import SIZE, POSITION, GUI_KEY

from unit.block import Block
from unit.zoning import Zoning
from unit.memory import Memory


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

        # self.memory = MAIN_MEMORY
        self.memory = Memory()
        self.update_data()

        self.resize(SIZE.WINDOW_WIDTH + 1, SIZE.WINDOW_HEIGHT + 1)
        self.setFixedSize(SIZE.WINDOW_WIDTH + 1, SIZE.WINDOW_HEIGHT + 1)
        self.setWindowTitle(f'Super Continent [{functions.game_time_to_date(0)}]')

        self.show()

    def update_data(self):
        # 根据memory更新界面
        for key, value in self.memory.dump().items():
            self.components[key].update(value)

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
            msg = ''
            if c_name == GUI_KEY.WORLD:
                block: Block = component.mouse_choose_item(event)
                msg = block.display()
                self.memory.update_block(block.ident)
            if c_name == GUI_KEY.ZONING:
                zoning: Zoning = component.mouse_choose_item(event)
                msg = zoning.display()
            if c_name == GUI_KEY.SELECT:
                select_item  = component.mouse_choose_item(event)
                msg = select_item.display()
            if c_name == GUI_KEY.FILTER:
                filter_type = component.mouse_choose_item(event)
                msg = filter_type.display()
            if c_name == GUI_KEY.PANEL:
                panel = component.mouse_choose_item(event)
                msg = panel.display()

            self.memory.msg = msg

        if click == Qt.RightButton:
            self.memory.msg = f"右键:\n{event.pos().x()}, {event.pos().y()}\n"
        self.update_data()
