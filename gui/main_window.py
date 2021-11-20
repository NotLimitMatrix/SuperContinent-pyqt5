from PyQt5.QtWidgets import QMainWindow

from reference.gui import SIZE


class MainGameGUI(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainGameGUI, self).__init__(*args, **kwargs)
        self.resize(SIZE.WINDOW_WIDTH + 1, SIZE.WINDOW_HEIGHT + 1)
        self.setFixedSize(SIZE.WINDOW_WIDTH + 1, SIZE.WINDOW_HEIGHT + 1)
        self.setWindowTitle('Super Continent')

        self.show()

    def init(self):
        pass
