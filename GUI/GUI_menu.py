from GUI import QAction,qApp, QMainWindow


class Menu:
    def __init__(self, parent):
        main_menu_bar = QMainWindow.menuBar(parent)

        exitAct = QAction('退出游戏', parent)
        exitAct.triggered.connect(qApp.quit)

        start_game = QAction("开始游戏", parent)
        load_data = QAction("载入存档", parent)
        export_data = QAction("保存存档", parent)
        net_game = QAction("联机对战", parent)

        game = main_menu_bar.addMenu('游戏')

        game.addAction(start_game)
        game.addAction(net_game)
        game.addAction(load_data)
        game.addAction(export_data)
        game.addAction(exitAct)
