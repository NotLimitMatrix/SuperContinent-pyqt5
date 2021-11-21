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
    # 科技领域种类: 经济、军工、超越
    TECHNOLOGY_TYPE = 3


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

    # 科技板宽度
    TECHNOLOGY_WIDTH = PANEL_WIDTH
    # 每个科技领域板的高度
    TECHNOLOGY_LEVEL_HEIGHT = PANEL_LEVEL_HEIGHT
    # 科技板高度
    TECHNOLOGY_HEIGHT = TECHNOLOGY_LEVEL_HEIGHT * NUMBER.TECHNOLOGY_TYPE

    # 区域间隔
    DX = 1

    # 窗口宽度
    WINDOW_WIDTH = DX + WORLD_WIDTH + DX * 2 + ZONING_WIDTH + DX * 2 + PANEL_WIDTH + DX
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
    ZONING_LEFT = WORLD_RIGHT + SIZE.DX * 2
    # 区划右边坐标
    ZONING_RIGHT = ZONING_LEFT + SIZE.ZONING_WIDTH

    # 面板顶部坐标
    PANEL_TOP = WORLD_TOP
    # 面板左边坐标
    PANEL_LEFT = ZONING_RIGHT + SIZE.DX * 2

    # 科技板顶部坐标
    TECHNOLOGY_TOP = PANEL_TOP + SIZE.PANEL_HEIGHT + SIZE.DX * 2
    # 科技板底部坐标
    TECHNOLOGY_BOTTOM = TECHNOLOGY_TOP + SIZE.PANEL_LEVEL_HEIGHT * NUMBER.TECHNOLOGY_TYPE
    # 科技板左边坐标
    TECHNOLOGY_LEFT = PANEL_LEFT
    # 科技板右边坐标
    TECHNOLOGY_RIGHT = TECHNOLOGY_LEFT + SIZE.TECHNOLOGY_WIDTH


# 颜色常量
class COLOR:
    WHITE = QColor(255, 255, 255)
    BLACK = QColor(0, 0, 0)
    GREEN = QColor(0, 255, 0)
    RED = QColor(255, 0, 0)
    BLUE = QColor(0, 0, 255)
    DIM_GREY = QColor(105, 105, 105)

    # 无色
    COLOR_LESS = QColor(0, 0, 0, 0)

    # 科技: 经济领域指定颜色
    TECH_ECONOMY = QColor(0, 255, 127)
    # 科技: 军工领域指定颜色
    TECH_MILITARY = QColor(0, 191, 255)
    # 科技: 超越领域指定颜色
    TECH_BEYOND = QColor(255, 215, 0)
