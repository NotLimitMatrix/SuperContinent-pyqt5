from GUI import (
    QTableWidget,
    QTableWidgetItem,
    QAbstractItemView,
    QFont,
    Qt,
    QPainter,
    QPolygon,
)

from STATIC.CONST import WORLD_WIDTH

from STATIC import METHOD
from STATIC.METHOD import Vector
from Block import Block


def draw_ellipse(painter: QPainter, x, y, ws):
    painter.drawEllipse(x + ws // 4, y + ws // 4, ws // 2, ws // 2)


def draw_three_angle(painter: QPainter, x, y, ws):
    polygon = QPolygon()
    polygon.setPoints(x + ws // 2, y + ws // 6, x + ws // 6, y + 5 * ws // 6, x + 5 * ws // 6, y + 5 * ws // 6)
    painter.drawPolygon(polygon)


def draw_which(painter: QPainter, _type, x, y, ws):
    if _type == 0:
        return
    if _type == 1:
        draw_ellipse(painter, x, y, ws)
    if _type == 2:
        draw_three_angle(painter, x, y, ws)


def draw_solt(painter: QPainter, solt1, solt2, px, py, ws):
    draw_which(painter, solt1, px, py, ws // 2)
    draw_which(painter, solt2, px + ws // 2, py, ws // 2)


def GenerateTable(parent, r, c, hSize, vSize):
    table = QTableWidget(parent)
    table.setRowCount(r)
    table.setColumnCount(c)
    table.horizontalHeader().setVisible(False)
    table.horizontalHeader().setDefaultSectionSize(hSize)
    table.horizontalHeader().setHighlightSections(False)
    table.verticalHeader().setVisible(False)
    table.verticalHeader().setDefaultSectionSize(vSize)
    table.verticalHeader().setHighlightSections(False)

    font = QFont()
    font.setPixelSize(11)

    for r_ in range(r):
        for c_, item in enumerate(QTableWidgetItem() for _ in range(c)):
            item.setTextAlignment(Qt.AlignCenter)
            item.setFont(font)
            table.setItem(r_, c_, item)

    # 设置 不可编辑
    table.setEditTriggers(QAbstractItemView.NoEditTriggers)
    # 设置 不可选择
    table.setSelectionMode(QAbstractItemView.NoSelection)

    return table


def new_world(size):
    rb = METHOD.RandomBlock()
    ws = WORLD_WIDTH // size
    b_list = []
    for i, b in enumerate(rb.new_world(size * size)):
        status_id, zoning_number = b
        x, y = METHOD.index_to_xy(i, size)
        b_list.append(Block(i, status_id, zoning_number, ws, METHOD.Vector(x, y)))

    return b_list


def AStar_path(world_list, n, startPoint: Vector, goalPoint: Vector):
    closedSet = []
    openSet = [startPoint]
    cameFrom = dict()
    gScore = {startPoint: 0}
    hScore = {startPoint: METHOD.heuristic_estimate_of_distance(startPoint, goalPoint)}
    fScore = {startPoint: hScore.get(startPoint)}
    while openSet:
        x = METHOD.lowset_fscore(fScore)
        if x == goalPoint:
            return reconstruct_path(cameFrom, goalPoint)
        openSet.remove(x)
        closedSet.append(x)
        for y in neighbor_nodes(world_list, n, x):
            if y in closedSet:
                continue

            tentative_gScore = gScore[x] + METHOD.m_distance(x, y)
            if y not in openSet:
                tentative_better = True
            elif tentative_gScore < gScore[y]:
                tentative_better = True
            else:
                tentative_better = False

            if tentative_better:
                cameFrom[y] = x
                gScore[y] = tentative_gScore
                hScore[y] = METHOD.heuristic_estimate_of_distance(y, goalPoint)
                fScore[y] = gScore[y] + hScore[y]
                openSet.append(y)

        return []


def neighbor_nodes(world_list, n, point: Vector):
    index = point.to_index(n)
    if not world_list[index]:
        return []

    points = [Vector(point.x, point.y),
              Vector(point.x - 1, point.y), Vector(point.x + 1, point.y),
              Vector(point.x, point.y - 1), Vector(point.x, point.y + 1)]

    for point in points:
        if point.x < 0 or point.y < 0 or point.x == n or point.y == n or not world_list[point.to_index(n)]:
            points.remove(point)
    return points


def reconstruct_path(came_from, current_node):
    result = [current_node]
    while current_node in came_from:
        temp = came_from[current_node]
        result.append(temp)
        current_node = temp
    return result
