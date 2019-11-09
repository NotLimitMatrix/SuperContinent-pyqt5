from static import *

class Producer:
    def __init__(self, material, rate):
        self.material = material
        self.rate = rate

    def product(self):
        return self.material

class Person:
    def __init__(self, job, produce, consumption):
        self.job = job
        self.procude = produce
        self.consumption = consumption

    def __repr__(self):
        return f"<Persion: {self.job}, product: {self.procude.material}/month>"


Electrician = Person('electrician',)