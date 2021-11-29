from abc import ABC

from PyQt5.QtGui import QPainter, QMouseEvent
from PyQt5.QtCore import QRect

from reference.gui import COLOR, SIZE
from reference.functions import draw_text, tr
from reference.templates import TEMPLATE_TECHNOLOGY
from reference import dictionary
from gui.gui_base import BaseGUI

TECH_AREA_USING_COLOR = {
    dictionary.CIVIL: COLOR.TECH_ECONOMY,
    dictionary.MILITARY: COLOR.TECH_MILITARY,
    dictionary.HYPER: COLOR.TECH_HYPER
}


class TechnologyUnitGUI(BaseGUI, ABC):
    def __init__(self, area, *args, **kwargs):
        super(TechnologyUnitGUI, self).__init__(*args, **kwargs)
        self.name = None
        self.area = area
        self.color = TECH_AREA_USING_COLOR[area]
        self.name = None
        self.schedule = 0
        self.total = 1
        self.per = 0

    def draw_schedule(self, schedule_width, painter: QPainter):
        painter.setBrush(self.color)
        painter.drawRect(self.left, self.top, schedule_width, self.height)

    def draw_other_rect(self, other_left, other_width, painter: QPainter):
        painter.setBrush(COLOR.WHITE)
        painter.drawRect(other_left, self.top, other_width, self.height)

    def draw(self, painter: QPainter):
        schedule_width = int(self.per * self.width) if self.schedule < self.total else self.total

        painter.setPen(COLOR.COLOR_LESS)
        self.draw_schedule(schedule_width, painter)
        self.draw_other_rect(self.left + schedule_width, self.width - schedule_width, painter)
        painter.setPen(COLOR.BLACK)

        big_rect = QRect(self.left, self.top, self.width, self.height)
        painter.setBrush(COLOR.COLOR_LESS)
        painter.drawRect(big_rect)
        draw_text(big_rect, f"{self.name}: {round(self.per * 100, 2)}%", painter)

    def update(self, name, schedule, total):
        self.name = name
        self.total = 1 if total == 0 else total
        self.schedule = schedule
        self.per = schedule / total
        return self.is_finished()

    def is_finished(self):
        if self.schedule < self.total:
            return False, 0
        else:
            return True, self.schedule - self.total

    def display(self):
        return TEMPLATE_TECHNOLOGY.format(
            area=tr(self.area),
            technology=self.name,
            schedule=self.schedule,
            total=self.total
        )


class TechnologyGUI(BaseGUI, ABC):
    def __init__(self, *args, **kwargs):
        super(TechnologyGUI, self).__init__(*args, **kwargs)

        self.tech_list = [
            # 经济科技
            TechnologyUnitGUI(area=dictionary.CIVIL,
                              top=self.top, left=self.left,
                              width=self.width, height=SIZE.TECHNOLOGY_LEVEL_HEIGHT),
            # 军事科技
            TechnologyUnitGUI(area=dictionary.MILITARY,
                              top=self.top + SIZE.TECHNOLOGY_LEVEL_HEIGHT, left=self.left,
                              width=self.width, height=SIZE.TECHNOLOGY_LEVEL_HEIGHT),
            # 超越科技
            TechnologyUnitGUI(area=dictionary.HYPER,
                              top=self.top + SIZE.TECHNOLOGY_LEVEL_HEIGHT * 2, left=self.left,
                              width=self.width, height=SIZE.TECHNOLOGY_LEVEL_HEIGHT)
        ]

    def update(self, data):
        for component, d in zip(self.tech_list, data):
            component.update(*d)

    def draw(self, painter: QPainter):
        for component in self.tech_list:
            component.draw(painter)

    def mouse_choose_item(self, event: QMouseEvent):
        index = (event.pos().y() - self.top) // SIZE.PANEL_LEVEL_HEIGHT
        if index >= len(self.tech_list):
            index = -1

        return self.tech_list[index]
