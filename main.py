import sys

from PyQt5.QtWidgets import QApplication

from gui.main_window import MainGameGUI
from reference.gui import COLOR
from player.player import Player

if __name__ == '__main__':
    app = QApplication(sys.argv)

    player0 = Player(0, 'Tester No.1', COLOR.RED)
    player1 = Player(1, 'Tester No.2', COLOR.GREEN)
    player2 = Player(2, 'Tester No.3', COLOR.BLUE)
    gui = MainGameGUI(player=player0)

    sys.exit(app.exec_())
