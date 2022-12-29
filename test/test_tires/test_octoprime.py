import unittest, sys

sys.path.insert(0, 'D:/Orange coast college study/Forage/Lyft - Backend component/forage-lyft-starter-repo')

from tires.octoprime_tires import Octoprime

class TestOctoprime(unittest.TestCase):
    def test_needs_service_true(self):
        current_tires = [0.8, 0.5, 0.9, 0.8]
        carTires = Octoprime(current_tires)
        self.assertTrue(carTires.needs_service())

    def test_needs_service_false(self):
        current_tires = [0.7, 0.6, 0.8, 0.9]
        carTires = Octoprime(current_tires)
        self.assertFalse(carTires.needs_service())

unittest.main()