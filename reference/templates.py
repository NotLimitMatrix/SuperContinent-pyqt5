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