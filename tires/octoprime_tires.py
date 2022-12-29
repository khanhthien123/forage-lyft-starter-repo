from tires.tires import Tires

class Octoprime(Tires):
    def __init__(self, tires_worn_degree):
        self.tires_worn_degree = tires_worn_degree

    def needs_service(self):
        return sum(self.tires_worn_degree) >= 3
        