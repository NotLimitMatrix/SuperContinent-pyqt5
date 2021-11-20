from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPainter
from PyQt5 import QtGui

from reference.gui import SIZE, NUMBER, POSITION

from gui.gui_world import WorldGUI


class MainGameGUI(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainGameGUI, self).__init__(*args, **kwargs)

        self.gui_world = WorldGUI(NUMBER.WORLD_NUMBER,
                                  top=POSITION.WORLD_TOP, left=POSITION.WORLD_LEFT,
                                  width=SIZE.WORLD_WIDTH, height=SIZE.WORLD_HEIGHT)

        self.resize(SIZE.WINDOW_WIDTH + 1, SIZE.WINDOW_HEIGHT + 1)
        self.setFixedSize(SIZE.WINDOW_WIDTH + 1, SIZE.WINDOW_HEIGHT + 1)
        self.setWindowTitle('Super Continent')

        self.show()

    def draw_window(self, painter: QPainter):
        self.gui_world.draw_component(painter)

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        p = QPainter()
        p.begin(self)
        self.draw_window(p)
        p.end()
