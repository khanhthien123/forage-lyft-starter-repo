import unittest, sys

sys.path.insert(0, 'D:/Orange coast college study/Forage/Lyft - Backend component/forage-lyft-starter-repo')

from tires.carrigan_tires import Carrigan

class TestCarrigan(unittest.TestCase):
    def test_needs_service_true(self):
        current_tires = [0.5, 0.2, 0.9, 0.8]
        carTires = Carrigan(current_tires)
        self.assertTrue(carTires.needs_service())

    def test_needs_service_false(self):
        current_tires = [0.5, 0.5, 0.5, 0.5]
        carTires = Carrigan(current_tires)
        self.assertFalse(carTires.needs_service())

unittest.main()