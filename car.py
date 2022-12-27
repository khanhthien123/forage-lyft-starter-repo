from serviceable import Serviceable
from battery.spindler import Spindler
from battery.nubbin import Nubbin
from engine.capulet import Capulet
from engine.sternman import Sternman
from engine.willoughby import Willoughby


class Car(Serviceable):
    def __init__(self, engine, battery):
        self.battery = battery
        self.engine = engine

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()

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
        return Car(newBattery, newEngine)

    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        newEngine = Willoughby(last_service_mileage, current_mileage)
        newBattery = Nubbin(last_service_date, current_date)
        return Car(newEngine, newBattery)

    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        newEngine = Capulet(last_service_mileage, current_mileage)
        newBattery = Nubbin(last_service_date, current_date)
        return Car(newEngine, newBattery)