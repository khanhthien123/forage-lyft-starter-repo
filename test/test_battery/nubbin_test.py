import unittest, sys

from datetime import date
sys.path.insert(0, 'D:/Orange coast college study/Forage/Lyft - Backend component/forage-lyft-starter-repo')
from battery.spindler import Spindler



class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        today = date(2020, 4, 4)
        last_service_date = date(2018, 4, 3)
        battery = Spindler(last_service_date, today)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        today = date(2020, 4, 4)
        last_service_date = date(2019, 3, 10)
        battery = Spindler(last_service_date, today)
        self.assertFalse(battery.needs_service())

unittest.main()