import unittest
from calculations import Calculations

class MyTestCase(unittest.TestCase):
    def test_eval1(self):
        calc = Calculations()
        x, y = calc.evaluation('x+5', -5, 5)
        # testing values of f(x) on boundries
        self.assertEqual(y[0], 0)
        self.assertEqual(y[-1], 10)

    def test_eval2(self):
        calc = Calculations()
        x, y = calc.evaluation('1/(x+3)', -5, 3)
        # testing values of f(x) on boundries
        self.assertEqual(y[0], -0.5)
        self.assertEqual(y[-1], 1/6)

    def test_eval3(self):
        calc = Calculations()
        x, y = calc.evaluation('1/(x+3)^2', -5, 3)
        # testing values of f(x) on boundries
        self.assertEqual(y[0], 0.25)
        self.assertEqual(y[-1], 1/36)




if __name__ == '__main__':
    unittest.main()


