from models import *

WORLD_SIZE = 30
BLOCK_SIZE = 6


def coordinate_to_index(i, j, size):
    return i * size + j


def index_to_coordinate(index, size):
    return divmod(index, size)


ALL_TECHNOLOGISTS = pkl_load("Models/technology.pkl")
ALL_KEYS = [k for k in ALL_TECHNOLOGISTS]

ALL_RESOURCE = pkl_load("Models/resources.pkl")
DYNAMIC_RESOURCE_PANEL = {k: v for k, v in ALL_RESOURCE.items() if 'dynamic' in k}
