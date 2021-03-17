from trash.models import *

ALL_TECHNOLOGISTS = pkl_load("Models/technology.pkl")
ALL_KEYS = [k for k in ALL_TECHNOLOGISTS]

ALL_RESOURCE = pkl_load("Models/resources.pkl")
DYNAMIC_RESOURCE_PANEL = {k: v for k, v in ALL_RESOURCE.items() if 'dynamic' in k}