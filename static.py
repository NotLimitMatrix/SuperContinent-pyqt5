from models import *


class CONST:
    WORLD_NUMBER = 20
    ZONING_NUMBER = 5

    WINDOW_WIDTH = 1000
    WINDOW_HEIGHT = 600

    WORLD_WIDTH = 600
    ZONING_WIDTH = 240

    WORLD_SQUARE_SIZE = WORLD_WIDTH // WORLD_NUMBER
    ZONING_SQUARE_SIZE = ZONING_WIDTH // ZONING_NUMBER

    WORLD_POSITION_START = 0
    WORLD_POSITION_END = WORLD_POSITION_START + 600

    ZONING_POSITION_START_X = WORLD_WIDTH + 5
    ZONING_POSITION_START_Y = WORLD_POSITION_START
    ZONING_POSITION_END_X = ZONING_POSITION_START_X + ZONING_WIDTH
    ZONING_POSITION_END_Y = ZONING_POSITION_START_Y + ZONING_WIDTH

    WAIT_PANEL_START_X = 605
    WAIT_PANEL_START_Y = 245
    WAIT_PANEL_WIDTH = 243
    WAIT_PANEL_HEIGHT = 355

    WINDOW_TITLE = "Super Continent"
    RESOURCE_PANELS = ("能量", "矿物", "食物", "物资", "合金")
    POWER_PANELS = ("经济", '军事', "科研")

    RIGHT_ALL_PANEL_START_X = 850

    RESOURCE_PANEL_START_X = RIGHT_ALL_PANEL_START_X
    RESOURCE_PANEL_START_Y = 1
    RESOURCE_PANEL_WIDTh = 148
    RESOURCE_PANEL_HEIGHT = 135

    POWER_PANEL_START_X = RIGHT_ALL_PANEL_START_X
    POWER_PANEL_START_Y = 131
    POWER_PANEL_WIDTH = 148
    POWER_PANEL_HEIGHT = 110

    RESEARCH_PANEL_START_X = RIGHT_ALL_PANEL_START_X
    RESEARCH_PANEL_START_Y = 246

    RESEARCH_LABEL_START_X = RESEARCH_PANEL_START_X
    RESEARCH_LABEL_START_Y = RESEARCH_PANEL_START_Y
    RESEARCE_LABEL_STYLE = "font: 10pt ;border-width: 1px;border-style: solid;border-color: rgb(0, 0, 0)"

    RESEARCH_RATE_BUTTON_START_X = RESEARCH_PANEL_START_X + 100
    RESEARCH_RATE_BUTTON_START_Y = RESEARCH_PANEL_START_Y - 6

    RESEARCH_TRANSFORM_START_X = RESEARCH_PANEL_START_X + 120
    RESEARCH_TRANSFORM_START_Y = RESEARCH_PANEL_START_Y - 6

    DETAIL_START_X = RIGHT_ALL_PANEL_START_X
    DETAIL_START_Y = 305
    DETAIL_WIDTH = 148
    DETAIL_HEIGHT = 295

    SPEED = 2
    TIME_FLOW = 1 / SPEED

    RESOURCE_WEIGHT = [(1, 5), (1, 5), (1, 5), (3, 10), (3, 10)]


def coordinate_to_index(i, j, size):
    return i * size + j


def index_to_coordinate(index, size):
    return divmod(index, size)


def format_number(number):
    if number > 1000000000:
        return "1G"
    elif number > 999999:
        return f"{number // 1000000}M"
    elif number > 999:
        return f"{number // 1000}K"
    else:
        return str(number)


def display_number(n, have_neg=True):
    if have_neg:
        number = abs(n)
        neg = '-' if n < 0 else '+'
        return f"{neg}{format_number(number)}"
    else:
        return format_number(n) if n > 0 else '0'


ALL_TECHNOLOGISTS = pkl_load("Models/technology.pkl")
ALL_KEYS = [k for k in ALL_TECHNOLOGISTS]

ALL_RESOURCE = pkl_load("Models/resources.pkl")
DYNAMIC_RESOURCE_PANEL = {k: v for k, v in ALL_RESOURCE.items() if 'dynamic' in k}
