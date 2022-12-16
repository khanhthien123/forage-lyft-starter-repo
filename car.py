from abc import ABC, abstractmethod
from datetime import date
from battery import Spindler, Nubbin
from carEngine import Capulet, Willoughby, Sternman


class Car(ABC):
    def __init__(self, engine, battery):
        self.battery = battery
        self.engine = engine

    @abstractmethod
    def needs_service(self):
        return self.engine.needs_service() and self.battery.needs_service()

class CarFactory():
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        newEngine = Capulet(last_service_mileage, current_mileage)
        newBattery = Spindler(last_service_date, current_date)
        return Car(newBattery, newEngine)

    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        newEngine = Willoughby(last_service_mileage, current_mileage)
        newBattery = Spindler(last_service_date, current_date)
        return Car(newBattery, newEngine)

    def create_palindrome(current_date, last_service_date, warning_light_on):
        newEngine = Sternman(warning_light_on)
        newBattery = Spindler(last_service_date, current_date)
        return Car(Sternman, Spindler)

    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        newEngine = Willoughby(last_service_mileage, current_mileage)
        newBattery = Nubbin(last_service_date, current_date)
        return Car(newEngine, newBattery)

    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        newEngine = Capulet(last_service_mileage, current_mileage)
        newBattery = Nubbin(last_service_date, current_date)
        return Car(newEngine, newBattery)