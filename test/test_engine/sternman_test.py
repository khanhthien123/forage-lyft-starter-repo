import unittest, sys

from datetime import date
sys.path.insert(0, 'D:/Orange coast college study/Forage/Lyft - Backend component/forage-lyft-starter-repo')

from engine.sternman import Sternman


class TestSternmanEngine(unittest.TestCase):
    def test_needs_service_true(self):
        warning_light_on = True
        engine = Sternman(warning_light_on)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        warning_light_on = False
        engine = Sternman(warning_light_on)
        self.assertFalse(engine.needs_service())

unittest.main()