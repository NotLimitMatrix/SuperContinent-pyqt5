TEMPLATE_BLOCK = """地块: {ident}
坐标: Row:{row}, Col:{col}
环境: {env_desc} {env_modifier}%
生产修正: {product_modifier}
维护花费: {upkeep_modifier}
"""

TEMPLATE_ZONING = """区划: {ident}
坐标: Row:{row}, Col:{col}
所属: {block_id}
建筑: {building}
"""

TEMPLATE_SELECT_ITEM = """备选项: {ident}
"""

TEMPLATE_FILTER = """滤镜: {filter_type}
"""

TEMPLATE_RESOURCE = """{resource}: {storage} {daily}
储备: {storage}
    国库: 10
    领地: {territory}
收入: {daily}
    税收: +10
    领地: +10
消耗:
    人口维护: -5
    土地利用: -5
"""

TEMPLATE_POWER = """{power}: {power_number}
人口: 10
"""
