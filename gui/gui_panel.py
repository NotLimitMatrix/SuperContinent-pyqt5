from abc import ABC
from typing import Iterable

from PyQt5.QtGui import QPainter, QMouseEvent
from PyQt5.QtCore import QRect

from reference.gui import COLOR, NUMBER, SIZE
from reference.functions import draw_text, tr
from reference.templates import TEMPLATE_RESOURCE, TEMPLATE_POWER
from reference import dictionary
from gui.gui_base import BaseGUI


class PanelResourceGUI(BaseGUI, ABC):
    def __init__(self, name, *args, **kwargs):
        super(PanelResourceGUI, self).__init__(*args, **kwargs)
        self.name = name

    def draw_resource(self, painter: QPainter, left, width, content):
        rect = QRect(left, self.top, width, self.height)
        painter.drawRect(rect)
        draw_text(rect, content, painter)

    def draw(self, painter: QPainter):
        painter.setBrush(COLOR.WHITE)

        width_name = int(self.width * NUMBER.PANEL_NAME_PER)
        width_storage = int(self.width * NUMBER.PANEL_STORAGE_PER)
        width_daily = int(self.width * NUMBER.PANEL_DAILY_PER)

        self.draw_resource(painter, self.left, width_name, tr(self.name))
        self.draw_resource(painter, self.left + width_name, width_storage, self.storage)
        self.draw_resource(painter, self.left + width_name + width_storage, width_daily, self.daily)

    def update(self, storage, daily):
        self.storage = storage
        self.daily = daily

    def display(self):
        return TEMPLATE_RESOURCE.format(
            resource=tr(self.name),
            storage=self.storage,
            daily=self.daily,
            territory=10 - self.storage
        )


class PanelPowerGUI(BaseGUI, ABC):
    def __init__(self, name, *args, **kwargs):
        super(PanelPowerGUI, self).__init__(*args, **kwargs)
        self.name = name

    def draw_power(self, painter: QPainter, left, width, content):
        rect = QRect(left, self.top, width, self.height)
        painter.drawRect(rect)
        draw_text(rect, content, painter)

    def draw(self, painter: QPainter):
        painter.setBrush(COLOR.WHITE)

        width_name = int(self.width * NUMBER.PANEL_NAME_PER)
        width_power = int(self.width * NUMBER.PANEL_POWER_PER)

        self.draw_power(painter, self.left, width_name, tr(self.name))
        self.draw_power(painter, self.left + width_name, width_power, self.power)

    def update(self, power):
        self.power = power

    def display(self):
        return TEMPLATE_POWER.format(
            power=tr(self.name),
            power_number=self.power
        )


def gen_panel_item(iter: Iterable, _class, parent, start=0):
    for index, it in enumerate(iter):
        yield _class(name=it, top=parent.top + SIZE.PANEL_LEVEL_HEIGHT * (start + index), left=parent.left,
                     width=parent.width, height=SIZE.PANEL_LEVEL_HEIGHT, parent=parent.parent)


class PanelGUI(BaseGUI, ABC):
    def __init__(self, *args, **kwargs):
        super(PanelGUI, self).__init__(*args, **kwargs)

        self.p_res = (dictionary.FOOD, dictionary.MINERAL, dictionary.ENERGY, dictionary.COMMODITY, dictionary.ALLOY)
        self.p_pow = (dictionary.POPULATION, dictionary.CIVIL, dictionary.MILITARY, dictionary.TECHNOLOGY)

        self.panels = list(gen_panel_item(self.p_res, PanelResourceGUI, self))
        self.panels.extend(gen_panel_item(self.p_pow, PanelPowerGUI, self, len(self.p_res)))

    def draw(self, painter: QPainter):
        painter.setBrush(COLOR.WHITE)
        for component in self.panels:
            component.draw(painter)

    def update(self, data):
        for component, d in zip(self.panels, data):
            if isinstance(d, int):
                component.update(d)
            else:
                component.update(*d)

    def mouse_choose_item(self, event: QMouseEvent):
        index = (event.pos().y() - self.top) // SIZE.PANEL_LEVEL_HEIGHT
        if index >= len(self.panels):
            index = -1

        return self.panels[index]
