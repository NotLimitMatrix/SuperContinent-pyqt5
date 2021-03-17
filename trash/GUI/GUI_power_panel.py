from GUI import (
    Static,
    CONST,
)


class GuiPowerPanel:
    def __init__(self, parent):
        table = Static.GenerateTable(parent, 3, 2, 73, 36)
        table.setGeometry(CONST.POWER_PANEL_START_X, CONST.POWER_PANEL_START_Y,
                          CONST.POWER_PANEL_WIDTH, CONST.POWER_PANEL_HEIGHT)
        self.table = table
        self.table_items = ['0', '0', '0']

    def check_items(self, items):
        if items:
            self.table_items = items.copy()
        else:
            self.table_items = ['0', '0', '0']

    def update(self, items: list):
        self.check_items(items)

        for row in range(3):
            self.table.item(row, 0).setText(CONST.POWER_PANELS[row])
            self.table.item(row, 1).setText(self.table_items[row])
