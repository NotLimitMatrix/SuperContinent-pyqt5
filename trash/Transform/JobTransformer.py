import os

from Transform.Transform import Transformer
from trash.models import Job, Consumption, Product, json_load
from STATIC.DIRECTORY import DIR_COMMON, DIR_MODELS

IN_FILE_JOB = 'jobs.json'
OUT_FILE_JOB = 'jobs.pkl'


class JobTransformer(Transformer):
    def init(self, l):
        self.input_file = os.path.join(DIR_COMMON, IN_FILE_JOB)
        self.output_file = os.path.join(DIR_MODELS, OUT_FILE_JOB)
        temp_d = json_load(self.input_file)
        for k, v in temp_d.items():
            name = l[k]
            produce_dict, consume_dict = v.get('produce'), v.get('consume')

            # 生产物资， 生产所需， 生产效率
            p_produce, p_material, p_rate = produce_dict.keys()
            p_produce_number = produce_dict.get(p_produce)
            p_material_key = produce_dict.get(p_material)
            p_rate_number = produce_dict.get(p_rate)

            producer = Product(material=p_produce, number=p_produce_number, rate=p_rate)

            consume = {
                "food": consume_dict.get("food"),
                "consumer_goods": consume_dict.get("consumer_goods"),
                p_material_key: (p_produce_number * p_rate_number) if p_material_key else 0
            }

            consumer = Consumption(materials=consume, rate=consume_dict.get('rate'))

            self._dict[k] = Job(name, producer, consumer)
