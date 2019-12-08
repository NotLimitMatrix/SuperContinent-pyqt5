import os

from Transform.Transform import Transformer
from models import Resource, json_load
from Core.DIRECTORY import DIR_COMMON, DIR_MODELS

IN_FILE_RESOURCES = 'resources.json'
OUT_FILE_RESOURCES = 'resources.pkl'


class ResourceTransformer(Transformer):
    def init(self, l):
        self.input_file = os.path.join(DIR_COMMON, IN_FILE_RESOURCES)
        self.output_file = os.path.join(DIR_MODELS, OUT_FILE_RESOURCES)

        temp_d = json_load(self.input_file)
        for k, v in temp_d.item():
            self._dict[k] = Resource(name=l[k], need=v.get('need'), rate=v.get('rate'))
