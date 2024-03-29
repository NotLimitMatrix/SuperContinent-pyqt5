from reference import dictionary as dt
from reference.functions import tr
from reference.gui import COLOR


def calculate_weight(*weights):
    sum_weight = sum(weights)
    return [round(100 * (weight / sum_weight), 2) for weight in weights]


class BLOCK:
    # 地块环境
    ENVIRONMENT = [0, 1, 2, 3, 4]
    # 环境权重
    ENV_WEIGHT = calculate_weight(6, 20, 51, 15, 4)
    # 环境名词
    WORD = (tr(dt.ENV__2), tr(dt.ENV__1), tr(dt.ENV_0), tr(dt.ENV_1), tr(dt.ENV_2))
    # 地块颜色
    COLOR = (COLOR.ENV__2, COLOR.ENV__1, COLOR.ENV_0, COLOR.ENV_1, COLOR.ENV_2)
    # 地块修正
    MODIFIER = (-0.5, -0.25, 0, 0.25, 0.5)


class ZONING:
    # 地块区划数
    ZONING_NUMBER = (4, 5, 6, 7)
    # 区划数权重
    ZONING_WEIGHT = calculate_weight(75, 30, 12, 1)


class TECH:
    # 科研默认分配比例
    RESEARCHER_RATES = (3, 3, 4)


class OPTIONS:
    # 工具栏选项
    TOOLS = (dt.CONSOLE,)
    # 过滤选项
    FILTERS = (dt.F_DEFAULT, dt.F_TERRITORY)


if __name__ == '__main__':
    print(BLOCK.ENV_WEIGHT)
