from PyQt5.QtGui import QColor


# 数据常数
class NUMBER:
    # 初始世界宽度
    WORLD_NUMBER = 10
    # 初始区划数量
    ZONING_NUMBER = 6
    # 面板层数：食物、矿物、能源、物资、合金、人口、经济、军事、科技
    PANEL_NUMBER = 9
    # 面板名称宽度比例
    PANEL_NAME_PER = 0.2
    # 面板储备宽度比例
    PANEL_STORAGE_PER = 0.4
    # 面板增长宽度比例
    PANEL_DAILY_PER = 0.4
    # 面板战力宽度比例
    PANEL_POWER_PER = 0.8


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
    PANEL_WIDTH = 200
    # 面板高度
    PANEL_HEIGHT = ZONING_HEIGHT
    # 面板每层高度
    PANEL_LEVEL_HEIGHT = PANEL_HEIGHT // NUMBER.PANEL_NUMBER
    # 区域间隔
    DX = 1

    # 窗口宽度
    WINDOW_WIDTH = DX + WORLD_WIDTH + DX + ZONING_WIDTH + DX + PANEL_WIDTH + DX
    # 窗口高度
    WINDOW_HEIGHT = DX + WORLD_WIDTH + DX


# 坐标常数
class POSITION:
    # 世界顶部坐标
    WORLD_TOP = SIZE.DX
    # 世界底部坐标
    WORLD_BOTTOM = WORLD_TOP + SIZE.WORLD_HEIGHT
    # 世界左边坐标
    WORLD_LEFT = SIZE.DX
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
    PANEL_BOTTOM = PANEL_TOP + SIZE.PANEL_HEIGHT
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
    DIM_GREY = QColor(105, 105, 105)
