from models import *


class CONST:
    WORLD_NUMBER = 10
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

    WINDOW_TITLE = "Super Continent"
    RESOURCE_PANELS = ("能量", "矿物", "食物", "物资", "合金")
    POWER_PANELS = ("经济", '军事', "科研")

    SPEED = 2
    TIME_FLOW = 1 / SPEED

    class TEST:
        resources = [(1000, -200), (1000, +312), (2000, +100), (9999999, +999999), (10000, -10)]


def coordinate_to_index(i, j, size):
    return i * size + j


def index_to_coordinate(index, size):
    return divmod(index, size)


def display_number(number):
    if number < 0:
        quit(0)
    elif number > 1000000000:
        return "1G"
    elif number > 999999:
        return f"{number // 1000000}M"
    elif number > 999:
        return f"{number // 1000}K"
    else:
        return str(number)


ALL_TECHNOLOGISTS = pkl_load("Models/technology.pkl")
ALL_KEYS = [k for k in ALL_TECHNOLOGISTS]

ALL_RESOURCE = pkl_load("Models/resources.pkl")
DYNAMIC_RESOURCE_PANEL = {k: v for k, v in ALL_RESOURCE.items() if 'dynamic' in k}
