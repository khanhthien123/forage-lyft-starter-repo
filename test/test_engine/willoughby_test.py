import unittest, sys

from datetime import date
sys.path.insert(0, 'D:/Orange coast college study/Forage/Lyft - Backend component/forage-lyft-starter-repo')

from engine.willoughby import Willoughby

class TestWilloughbyEngine(unittest.TestCase):
    def test_needs_service_true(self):
        current_mileage = 60001
        last_service_mileage = 0
        engine = Willoughby(last_service_mileage, current_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        current_mileage = 60000
        last_service_mileage = 0
        engine = Willoughby(last_service_mileage, current_mileage)
        self.assertFalse(engine.needs_service())

unittest.main()