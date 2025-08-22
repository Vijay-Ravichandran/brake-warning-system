import unittest
from brake_light import check_brake_fluid
class TestBrakeLight(unittest.TestCase):
    def test_fluid_below_20(self):
        result = check_brake_fluid(15)
        self.assertEqual(result, "ON")

    def test_fluid_above_20(self):
        result = check_brake_fluid(75)
        self.assertEqual(result, "OFF")

    def test_fluid_at_20(self):
        result = check_brake_fluid(20)
        self.assertEqual(result, "OFF")

    def test_fluid_invalid_negative(self):
        result = check_brake_fluid(-1)
        self.assertEqual(result, "ERROR")

    def test_fluid_invalid_above_100(self):
        result = check_brake_fluid(101)
        self.assertEqual(result, "ERROR")
    
# if __name__ == "__main__":
    # unittest.main()