from abc import abstractmethod
from datetime import date

class Battery():
    @abstractmethod
    def needs_service():
        pass

class Spindler(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        diff = self.current_date.toordinal() - self.last_service_date.toordinal()
        return diff // 365 >= 2


class Nubbin(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        diff = self.current_date.toordinal() - self.last_service_date.toordinal()
        return diff // 365 >= 4