import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODELS = 'Models'
COMMON = 'Common'
C_BUILDING = 'Building'
C_LOCALISATION = 'Localisation'
C_TECHNOLOGY = 'Technology'

DIR_COMMON = os.path.join(PROJECT_ROOT, COMMON)
DIR_MODELS = os.path.join(PROJECT_ROOT, MODELS)
DIR_BUILDING = os.path.join(DIR_COMMON, C_BUILDING)
DIR_LOCALISATION = os.path.join(DIR_COMMON, C_LOCALISATION)
DIR_TECHNOLOGY = os.path.join(DIR_COMMON, C_TECHNOLOGY)

if __name__ == '__main__':
    print(PROJECT_ROOT)
    print(DIR_COMMON)
    print(DIR_MODELS)
    print(DIR_BUILDING)
    print(DIR_LOCALISATION)
    print(DIR_TECHNOLOGY)
