from GUI import QAction, qApp, QMainWindow, QInputDialog, QMenu


class Menu:
    def __init__(self, parent):
        main_menu_bar = parent.menuBar()
        self.parent = parent

        exitAct = QAction('退出游戏', parent)
        exitAct.triggered.connect(qApp.quit)

        start_game = QAction("开始游戏", parent)
        start_game.triggered.connect(self.NewGameDialog)

        load_data = QAction("载入存档", parent)
        export_data = QAction("保存存档", parent)

        net_game = QMenu("联机对战", parent)
        net_server_game = QAction("做为主机", parent)
        net_client_game = QAction("加入游戏", parent)
        net_game.addAction(net_server_game)
        net_game.addAction(net_client_game)

        game = main_menu_bar.addMenu('游戏')

        game.addAction(start_game)
        game.addMenu(net_game)
        game.addAction(load_data)
        game.addAction(export_data)
        game.addAction(exitAct)

    def NewGameDialog(self):
        text, ok = QInputDialog.getText(self.parent, "新建游戏", "地图尺寸")
        if ok:
            wn = int(text)
            self.parent.NewGame(wn)
