from battery.battery import Battery

class Nubbin(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        dateBatteryShouldBeServiced = self.last_service_date.replace(year=self.last_service_date.year + 4)
        return dateBatteryShouldBeServiced < self.current_date