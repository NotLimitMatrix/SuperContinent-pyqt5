from abc import ABC

from PyQt5.QtGui import QPainter
from PyQt5.QtCore import QRect

from reference.gui import COLOR, NUMBER, SIZE
from reference.functions import draw_text, tr
from reference import dictionary
from gui.gui_base import BaseGUI


class PanelResourceGUI(BaseGUI, ABC):
    def __init__(self, *args, **kwargs):
        super(PanelResourceGUI, self).__init__(*args, **kwargs)

    def draw_resource(self, painter: QPainter, left, width, content):
        rect = QRect(left, self.top, width, self.height)
        painter.drawRect(rect)
        draw_text(rect, content, painter)

    def draw(self, name, painter: QPainter):
        painter.setBrush(COLOR.WHITE)

        width_name = int(self.width * NUMBER.PANEL_NAME_PER)
        width_storage = int(self.width * NUMBER.PANEL_STORAGE_PER)
        width_daily = int(self.width * NUMBER.PANEL_DAILY_PER)

        self.draw_resource(painter, self.left, width_name, name)
        self.draw_resource(painter, self.left + width_name, width_storage, self.storage)
        self.draw_resource(painter, self.left + width_name + width_storage, width_daily, self.daily)

    def update(self, storage, daily):
        self.storage = storage
        self.daily = daily


class PanelPowerGUI(BaseGUI, ABC):
    def __init__(self, *args, **kwargs):
        super(PanelPowerGUI, self).__init__(*args, **kwargs)

    def draw_power(self, painter: QPainter, left, width, content):
        rect = QRect(left, self.top, width, self.height)
        painter.drawRect(rect)
        draw_text(rect, content, painter)

    def draw(self, name, painter: QPainter):
        painter.setBrush(COLOR.WHITE)

        width_name = int(self.width * NUMBER.PANEL_NAME_PER)
        width_power = int(self.width * NUMBER.PANEL_POWER_PER)

        self.draw_power(painter, self.left, width_name, name)
        self.draw_power(painter, self.left + width_name, width_power, self.power)

    def update(self, power):
        self.power = power


class PanelGUI(BaseGUI, ABC):
    def __init__(self, *args, **kwargs):
        super(PanelGUI, self).__init__(*args, **kwargs)

        self.panels = {
            # 食物
            dictionary.FOOD: PanelResourceGUI(top=self.top, left=self.left,
                                              width=self.width, height=SIZE.PANEL_LEVEL_HEIGHT),
            # 矿物
            dictionary.MINERAL: PanelResourceGUI(top=self.top + SIZE.PANEL_LEVEL_HEIGHT,
                                                 left=self.left,
                                                 width=self.width, height=SIZE.PANEL_LEVEL_HEIGHT),
            # 能源
            dictionary.ENERGY: PanelResourceGUI(top=self.top + SIZE.PANEL_LEVEL_HEIGHT * 2,
                                                left=self.left,
                                                width=self.width, height=SIZE.PANEL_LEVEL_HEIGHT),
            # 物资
            dictionary.COMMODITY: PanelResourceGUI(top=self.top + SIZE.PANEL_LEVEL_HEIGHT * 3, left=self.left,
                                                   width=self.width, height=SIZE.PANEL_LEVEL_HEIGHT),
            # 合金
            dictionary.ALLOY: PanelResourceGUI(top=self.top + SIZE.PANEL_LEVEL_HEIGHT * 4,
                                               left=self.left,
                                               width=self.width, height=SIZE.PANEL_LEVEL_HEIGHT),
            # 人口
            dictionary.POPULATION: PanelPowerGUI(top=self.top + SIZE.PANEL_LEVEL_HEIGHT * 5, left=self.left,
                                                 width=self.width, height=SIZE.PANEL_LEVEL_HEIGHT),
            # 经济
            dictionary.ECONOMY: PanelPowerGUI(top=self.top + SIZE.PANEL_LEVEL_HEIGHT * 6, left=self.left,
                                              width=self.width, height=SIZE.PANEL_LEVEL_HEIGHT),
            # 军力
            dictionary.MILITARY: PanelPowerGUI(top=self.top + SIZE.PANEL_LEVEL_HEIGHT * 7, left=self.left,
                                               width=self.width, height=SIZE.PANEL_LEVEL_HEIGHT),
            # 科技
            dictionary.TECHNOLOGY: PanelPowerGUI(top=self.top + SIZE.PANEL_LEVEL_HEIGHT * 8, left=self.left,
                                                 width=self.width, height=SIZE.PANEL_LEVEL_HEIGHT)
        }

    def draw(self, painter: QPainter):
        painter.setBrush(COLOR.WHITE)
        for p_name, p_component in self.panels.items():
            p_component.draw(tr(p_name), painter)

    def update(self, data):
        for title in data:
            d = data[title]
            if isinstance(d, int):
                self.panels[title].update(d)
            else:
                self.panels[title].update(*data[title])
