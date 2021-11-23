import os

from Transform.Transform import Transformer
from trash.models import SwordArmor, Technology, json_load
from STATIC.DIRECTORY import DIR_MODELS, DIR_TECHNOLOGY

DIR_SWORD_ARMOR = 'SwordArmor'
IN_FILE_TECHNOLOGY_MILITARY = 'military_technology.json'
IN_FILE_TECHNOLOGY_CIVIL = 'civil_technology.json'
IN_FILE_TECHNOLOGY_BEYOND = 'beyond_technology.json'
OUT_FILE_TECHNOLOGY = 'technology.pkl'


class TechnologyTransformer(Transformer):
    def init(self, l):
        self.files = [
            os.path.join(DIR_TECHNOLOGY, IN_FILE_TECHNOLOGY_MILITARY),
            os.path.join(DIR_TECHNOLOGY, IN_FILE_TECHNOLOGY_CIVIL),
            os.path.join(DIR_TECHNOLOGY, IN_FILE_TECHNOLOGY_BEYOND)
        ]
        self.output_file = os.path.join(DIR_MODELS, OUT_FILE_TECHNOLOGY)

    def transform_beyond_technology(self, l):
        Beyond = os.path.join(DIR_TECHNOLOGY, "beyond_technology.json")
        for k, v in self.gen_technologists(json_load(Beyond)):
            self._dict[k] = Technology(
                name=l[k],
                cost=v.get('cost'),
                front=v.get('front'),
                _type=v.get('type'),
                loop=False,
                no=v.get('no'),
                key=k
            )

    def transform_sword_armor(self, l):
        Sword_Armor = join(self.dir, "SwordArmor")
        for file in listdir(Sword_Armor):
            for k, v in self.gen_technologists(json_load(join(Sword_Armor, file))):

                *_, level = k.split('_')
                if level == 'x':
                    loop = True
                    level = 6
                else:
                    loop = False
                    level = int(level)

                self._dict[k] = SwordArmor(
                    name=l[k],
                    cost=v.get('cost'),
                    front=v.get('front'),
                    _type=v.get('type'),
                    no=v.get('no'),
                    loop=loop,
                    level=level,
                    key=k
                )
