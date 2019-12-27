from GUI import (
    QPainter,
    QPolygon,
)


class Shape:
    def __init__(self, t, ws):
        self.t = t
        self.ws = ws
        self.color = None

    def ellipase(self, painter: QPainter, px, py):
        painter.drawEllipse(px + self.ws // 4, py + self.ws // 4, self.ws // 2, self.ws // 2)

    def three_angle(self, painter: QPainter, px, py):
        polygon = QPolygon()
        polygon.setPoints(px + self.ws // 2, py + self.ws // 6,
                          px + self.ws // 6, py + 5 * self.ws // 6,
                          px + 5 * self.ws // 6, py + 5 * self.ws // 6)
        painter.drawPolygon(polygon)

    def draw(self, painter: QPainter, px, py):
        if self.t == 1:
            self.ellipase(painter, px, py)
        if self.t == 2:
            self.three_angle(painter, px, py)
