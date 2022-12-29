import unittest, sys

from datetime import date
sys.path.insert(0, 'D:/Orange coast college study/Forage/Lyft - Backend component/forage-lyft-starter-repo')

from engine.capulet import Capulet

class TestCapuletEngine(unittest.TestCase):
    def test_needs_service_true(self):
        current_mileage = 60001
        last_service_mileage = 30000
        engine = Capulet(last_service_mileage, current_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        current_mileage = 60000
        last_service_mileage = 30000
        engine = Capulet(last_service_mileage, current_mileage)
        self.assertFalse(engine.needs_service())


unittest.main()