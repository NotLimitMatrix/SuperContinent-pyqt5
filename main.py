import sys

from PyQt5.QtWidgets import QApplication

from gui.main_window import MainGameGUI
from reference.gui import COLOR
from player.player import Player

if __name__ == '__main__':
    app = QApplication(sys.argv)

    player = Player(0, 'Tester', COLOR.RED)
    gui = MainGameGUI(player)

    sys.exit(app.exec_())
