from tires.tires import Tires

class Carrigan(Tires):
    def __init__(self, tires_worn_degree):
        self.tires_worn_degree = tires_worn_degree

    def needs_service(self):
        for tire in self.tires_worn_degree:
            if tire >= 0.9:
                return True

        return False