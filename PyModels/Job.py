class Product:
    def __init__(self, material, number, rate):
        self.material = material
        self.number = number
        self.rate = rate

    def product(self):
        return {
            self.material: self.number * (1 + self.rate)
        }

    def gen(self):
        for k, v in self.product().items():
            yield k, v


class Consumption:
    def __init__(self, materials: dict, rate):
        self.materials = materials
        self.rate = rate

    def consume(self):
        return {
            k: v * (1 + self.rate) for k, v in self.materials.items()
        }

    def gen(self):
        for k, v in self.consume().items():
            yield k, v


class Job:
    def __init__(self, name, key, producer: Product, consumer: Consumption, rate):
        self.name = name
        self.key = key
        self.producer = producer
        self.consumer = consumer

    def produce_consume(self, made):
        # made: 0:consumption, 1:produce
        return {
            k: v for k, v in (self.producer.gen() if made else self.consumer.gen())
        }

    def __repr__(self):
        return f"<Job: {self.name}: Product:{self.producer.material}, Consumption:{[k for k in self.consumer.materials]}"
