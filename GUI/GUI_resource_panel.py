from GUI import (
    Static,
    CONST,
)


class GuiResourcePanel:
    def __init__(self, parent):
        table = Static.GenerateTable(parent, 5, 3, 48, 26)
        table.setGeometry(CONST.RESOURCE_PANEL_START_X, CONST.RESOURCE_PANEL_START_Y,
                          CONST.RESOURCE_PANEL_WIDTh, CONST.RESOURCE_PANEL_HEIGHT)
        self.table = table
        self.table_items = [['0', '0'], ['0', '0'], ['0', '0'], ['0', '0'], ['0', '0']]

    def check_items(self, items):
        if items:
            self.table_items = items.copy()
        else:
            self.table_items = [['0', '0'], ['0', '0'], ['0', '0'], ['0', '0'], ['0', '0']]

    def update(self, items: list):
        self.check_items(items)

        for raw in range(5):
            stroage, daily = self.table_items[raw]
            self.table.item(raw, 0).setText(CONST.RESOURCE_PANELS[raw])
            self.table.item(raw, 1).setText(stroage)
            self.table.item(raw, 2).setText(daily)
