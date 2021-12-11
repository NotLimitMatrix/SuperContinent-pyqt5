from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import QTextBrowser, QLineEdit, QVBoxLayout, QDialog
from PyQt5.QtCore import pyqtSignal


class ConsoleWidget(QDialog):
    _close_single = pyqtSignal()
    _send_command = pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        super(ConsoleWidget, self).__init__(*args, **kwargs)

        self.resize(900, 700)
        self.setFixedSize(900, 700)
        self.setWindowTitle('Super Continent Console')

        self.text_browser = QTextBrowser(parent=self)
        self.line_edit = QLineEdit(parent=self)
        self.line_edit.returnPressed.connect(self.command)

        self.init()
        self.show()

    def closeEvent(self, a0: QCloseEvent) -> None:
        self._close_single.emit()

    def init(self):
        layout = QVBoxLayout(self)
        layout.addWidget(self.text_browser)
        layout.addWidget(self.line_edit)
        self.setLayout(layout)

    def command(self):
        cmd = self.line_edit.text()
        self.line_edit.clear()
        match cmd:
            case 'clear':
                self.text_browser.clear()
            case 'close':
                self.close()
            case _:
                self.text_browser.append(cmd)
                self._send_command.emit(cmd)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)

    gui = ConsoleWidget()

    sys.exit(app.exec_())
