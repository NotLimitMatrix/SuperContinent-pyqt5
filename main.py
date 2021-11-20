import sys

from PyQt5.QtWidgets import QApplication

from gui.main_window import MainGameGUI

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = MainGameGUI()
    sys.exit(app.exec_())
