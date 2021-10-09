from temp import Temperature
import unittest
class Mytest(unittest.TestCase):
    #Test to see self.kevin = kelvin
    # Should be ok if values are equal
    def test_kelvin(self):
        self.assertEqual(Temperature(273).kelvin, 273)

    #Test if having no argument raises the Value error
    # Should be ok if it raised the Value error
    def test_no_argument(self):
        with self.assertRaises(ValueError):
            Temperature()

    #Test if having more than 1 argument raises the Value error
    # Should be ok if it raised the Value error
    def test_many_argument(self):
        with self.assertRaises(ValueError):
            Temperature(1,2,3)

    #Test if having negative argument raises the Value error
    # Should be ok if it raised the Value error
    def test_negative_argument(self):
        with self.assertRaises(ValueError):
            Temperature(-1)

if __name__ == "__main__":
    unittest.main()