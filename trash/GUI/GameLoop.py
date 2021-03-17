import time

from GUI import pyqtSignal, QObject, CONST


class GameLoop(QObject):
    updater = pyqtSignal(dict)

    def __init__(self, main_process, *args, **kwargs):
        self.main_process = main_process
        super().__init__(*args, **kwargs)

    def recv(self, content: dict):
        content = content.copy()
        print(content)

    def run(self):
        while True:
            content = self.main_process.display()
            self.updater.emit(content)
            time.sleep(CONST.TIME_FLOW)
