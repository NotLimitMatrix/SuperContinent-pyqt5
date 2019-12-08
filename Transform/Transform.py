from models import pkl_dump

from Transform.Localisation import Localisation


class Transformer:
    def __init__(self):
        self._dict = dict()
        self.input_file = None
        self.output_file = None
        self.localisation = Localisation()

    def init(self, l):
        pass

    def transform(self):
        pkl_dump(self._dict, self.output_file)
