from PyQt5.QtGui import QColor


# 数据常数
class NUMBER:
    # 初始世界宽度
    WORLD_NUMBER = 10
    # 初始区划数量
    ZONING_NUMBER = 1


# 尺寸常数
class SIZE:
    # 世界宽度
    WORLD_WIDTH = 700
    # 世界高度
    WORLD_HEIGHT = WORLD_WIDTH

    # 区划宽度
    ZONING_WIDTH = 300
    # 区划高度
    ZONING_HEIGHT = ZONING_WIDTH

    # 面板宽度
    PANEL_WIDTH = 300

    # 区域间隔
    DX = 1

    # 窗口宽度
    WINDOW_WIDTH = WORLD_WIDTH + DX + ZONING_WIDTH + DX + PANEL_WIDTH
    # 窗口高度
    WINDOW_HEIGHT = WORLD_WIDTH


# 坐标常数
class POSITION:
    # 世界顶部坐标
    WORLD_TOP = 0
    # 世界底部坐标
    WORLD_BOTTOM = WORLD_TOP + SIZE.WORLD_HEIGHT
    # 世界左边坐标
    WORLD_LEFT = 0
    # 世界右边坐标
    WORLD_RIGHT = WORLD_LEFT + SIZE.WORLD_WIDTH

    # 区划顶部坐标
    ZONING_TOP = WORLD_TOP
    # 区划底部坐标
    ZONING_BOTTOM = ZONING_TOP + SIZE.ZONING_HEIGHT
    # 区划左边坐标
    ZONING_LEFT = WORLD_RIGHT + SIZE.DX
    # 区划右边坐标
    ZONING_RIGHT = ZONING_LEFT + SIZE.ZONING_WIDTH

    # 面板顶部坐标
    PANEL_TOP = WORLD_TOP
    # 面板底部坐标
    # 面板左边坐标
    PANEL_LEFT = ZONING_RIGHT + SIZE.DX
    # 面板右边坐标
    PANEL_RIGHT = PANEL_LEFT + SIZE.PANEL_WIDTH


# 颜色常量
class COLOR:
    WHITE = QColor(255, 255, 255)
    BLACK = QColor(0, 0, 0)
    GREEN = QColor(0, 255, 0)
    RED = QColor(255, 0, 0)
    BLUE = QColor(0, 0, 255)
