from serviceable import Serviceable
from battery.spindler import Spindler
from battery.nubbin import Nubbin
from engine.capulet import Capulet
from engine.sternman import Sternman
from engine.willoughby import Willoughby
from tires.carrigan_tires import Carrigan
from tires.octoprime_tires import Octoprime

class Car(Serviceable):
    def __init__(self, engine, battery, tires):
        self.battery = battery
        self.engine = engine
        self.tires = tires

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()

class CarFactory():
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tires_worn_degree):
        newEngine = Capulet(last_service_mileage, current_mileage)
        newBattery = Spindler(last_service_date, current_date)
        newTiresWornDegree = Carrigan(tires_worn_degree)
        return Car(newBattery, newEngine, newTiresWornDegree)

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tires_worn_degree):
        newEngine = Willoughby(last_service_mileage, current_mileage)
        newBattery = Spindler(last_service_date, current_date)
        newTiresWornDegree = Carrigan(tires_worn_degree)
        return Car(newBattery, newEngine, newTiresWornDegree)

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on, tires_worn_degree):
        newEngine = Sternman(warning_light_on)
        newBattery = Spindler(last_service_date, current_date)
        newTiresWornDegree = Octoprime(tires_worn_degree)
        return Car(newBattery, newEngine, newTiresWornDegree)

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tires_worn_degree):
        newEngine = Willoughby(last_service_mileage, current_mileage)
        newBattery = Nubbin(last_service_date, current_date)
        newTiresWornDegree = Octoprime(tires_worn_degree)
        return Car(newBattery, newEngine, newTiresWornDegree)

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tires_worn_degree):
        newEngine = Capulet(last_service_mileage, current_mileage)
        newBattery = Nubbin(last_service_date, current_date)
        newTiresWornDegree = Octoprime(tires_worn_degree)
        return Car(newBattery, newEngine, newTiresWornDegree)