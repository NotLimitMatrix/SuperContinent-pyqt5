from reference import dictionary as dt
from reference.functions import tr
from reference.gui import COLOR


class BLOCK:
    # 地块环境
    ENVIRONMENT = [-2, -1, 0, 1, 2]
    # 环境权重
    ENV_WEIGHT = (5, 23, 60, 9, 3)
    # 环境名词
    WORD = (tr(dt.ENV__2), tr(dt.ENV__1), tr(dt.ENV_0), tr(dt.ENV_1), tr(dt.ENV_2))
    # 地块颜色
    COLOR = (COLOR.ENV__2, COLOR.ENV__1, COLOR.ENV_0, COLOR.ENV_1, COLOR.ENV_2)
    # 地块修正
    MODIFIER = (-0.5, -0.25, 0, 0.25, 0.5)
    # 地块区划数
    ZONING_NUMBER = (3, 4, 5, 6)


# 科研默认分配比例
RESEARCHER_RATES = (3, 3, 4)
