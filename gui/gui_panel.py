from abc import ABC

from PyQt5.QtGui import QPainter
from PyQt5.QtCore import QRect

from reference.gui import COLOR, NUMBER, SIZE
from reference.functions import draw_text, tr
from reference import dictionary
from gui.gui_base import BaseGUI


class PanelResourceGUI(BaseGUI, ABC):
    def __init__(self, name, storage, daily, *args, **kwargs):
        super(PanelResourceGUI, self).__init__(*args, **kwargs)
        self.name = name
        self.storage = storage
        self.daily = daily

    def draw_resource(self, painter: QPainter, left, width, content):
        rect = QRect(left, self.top, width, self.height)
        painter.drawRect(rect)
        draw_text(rect, content, painter)

    def draw_component(self, painter: QPainter):
        painter.setBrush(COLOR.WHITE)

        width_name = int(self.width * NUMBER.PANEL_NAME_PER)
        width_storage = int(self.width * NUMBER.PANEL_STORAGE_PER)
        width_daily = int(self.width * NUMBER.PANEL_DAILY_PER)

        self.draw_resource(painter, self.left, width_name, self.name)
        self.draw_resource(painter, self.left + width_name, width_storage, self.storage)
        self.draw_resource(painter, self.left + width_name + width_storage, width_daily, self.daily)

    def update(self):
        pass


class PanelPowerGUI(BaseGUI, ABC):
    def __init__(self, name, power, *args, **kwargs):
        super(PanelPowerGUI, self).__init__(*args, **kwargs)
        self.name = name
        self.power = power

    def draw_power(self, painter: QPainter, left, width, content):
        rect = QRect(left, self.top, width, self.height)
        painter.drawRect(rect)
        draw_text(rect, content, painter)

    def draw_component(self, painter: QPainter):
        painter.setBrush(COLOR.WHITE)

        width_name = int(self.width * NUMBER.PANEL_NAME_PER)
        width_power = int(self.width * NUMBER.PANEL_POWER_PER)

        self.draw_power(painter, self.left, width_name, self.name)
        self.draw_power(painter, self.left + width_name, width_power, self.power)

    def update(self):
        pass


class PanelGUI(BaseGUI, ABC):
    def __init__(self, *args, **kwargs):
        super(PanelGUI, self).__init__(*args, **kwargs)

        self.panels_resource = [
            # 食物
            PanelResourceGUI(tr(dictionary.FOOD), 0, 0, top=self.top, left=self.left,
                             width=self.width, height=SIZE.PANEL_LEVEL_HEIGHT),
            # 矿物
            PanelResourceGUI(tr(dictionary.MINERAL), 0, 0, top=self.top + SIZE.PANEL_LEVEL_HEIGHT, left=self.left,
                             width=self.width, height=SIZE.PANEL_LEVEL_HEIGHT),
            # 能源
            PanelResourceGUI(tr(dictionary.ENERGY), 0, 0, top=self.top + SIZE.PANEL_LEVEL_HEIGHT * 2, left=self.left,
                             width=self.width, height=SIZE.PANEL_LEVEL_HEIGHT),
            # 物资
            PanelResourceGUI(tr(dictionary.COMMODITY), 0, 0, top=self.top + SIZE.PANEL_LEVEL_HEIGHT * 3, left=self.left,
                             width=self.width, height=SIZE.PANEL_LEVEL_HEIGHT),
            # 合金
            PanelResourceGUI(tr(dictionary.ALLOY), 0, 0, top=self.top + SIZE.PANEL_LEVEL_HEIGHT * 4, left=self.left,
                             width=self.width, height=SIZE.PANEL_LEVEL_HEIGHT)
        ]

        self.panels_power = [
            # 人口
            PanelPowerGUI(tr(dictionary.POPULATION), 10, top=self.top + SIZE.PANEL_LEVEL_HEIGHT * 5, left=self.left,
                          width=self.width, height=SIZE.PANEL_LEVEL_HEIGHT),
            # 经济
            PanelPowerGUI(tr(dictionary.ECONOMY), 10, top=self.top + SIZE.PANEL_LEVEL_HEIGHT * 6, left=self.left,
                          width=self.width, height=SIZE.PANEL_LEVEL_HEIGHT),
            # 军力
            PanelPowerGUI(tr(dictionary.MILITARY), 10, top=self.top + SIZE.PANEL_LEVEL_HEIGHT * 7, left=self.left,
                          width=self.width, height=SIZE.PANEL_LEVEL_HEIGHT),
            # 科技
            PanelPowerGUI(tr(dictionary.TECHNOLOGY), 10, top=self.top + SIZE.PANEL_LEVEL_HEIGHT * 8, left=self.left,
                          width=self.width, height=SIZE.PANEL_LEVEL_HEIGHT)
        ]

    def draw_component(self, painter: QPainter):
        painter.setBrush(COLOR.WHITE)
        for component_resource in self.panels_resource:
            component_resource.draw_component(painter)
        for component_power in self.panels_power:
            component_power.draw_component(painter)

    def update(self):
        pass
