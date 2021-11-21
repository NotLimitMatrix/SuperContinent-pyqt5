from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPainter
from PyQt5 import QtGui

from reference.gui import SIZE, NUMBER, POSITION

from gui.gui_world import WorldGUI
from gui.gui_zoning import ZoningGUI
from gui.gui_panel import PanelGUI


class MainGameGUI(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainGameGUI, self).__init__(*args, **kwargs)

        self.gui_world = WorldGUI(NUMBER.WORLD_NUMBER,
                                  top=POSITION.WORLD_TOP, left=POSITION.WORLD_LEFT,
                                  width=SIZE.WORLD_WIDTH, height=SIZE.WORLD_HEIGHT)
        self.gui_zoning = ZoningGUI(NUMBER.ZONING_NUMBER,
                                    top=POSITION.ZONING_TOP, left=POSITION.ZONING_LEFT,
                                    width=SIZE.ZONING_WIDTH, height=SIZE.ZONING_HEIGHT)
        self.gui_panel = PanelGUI(top=POSITION.PANEL_TOP, left=POSITION.PANEL_LEFT,
                                  width=SIZE.PANEL_WIDTH, height=SIZE.PANEL_HEIGHT)

        self.resize(SIZE.WINDOW_WIDTH + 1, SIZE.WINDOW_HEIGHT + 1)
        self.setFixedSize(SIZE.WINDOW_WIDTH + 1, SIZE.WINDOW_HEIGHT + 1)
        self.setWindowTitle('Super Continent')

        self.show()

    def draw_window(self, painter: QPainter):
        self.gui_world.draw_component(painter)
        self.gui_zoning.draw_component(painter)
        self.gui_panel.draw_component(painter)

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        p = QPainter()
        p.begin(self)
        self.draw_window(p)
        p.end()
