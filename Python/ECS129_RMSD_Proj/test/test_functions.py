import unittest
from src import functions
import numpy as np


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def test_something(self):
        self.assertEqual(True, False)

    def test_something(self):
        self.assertEqual(True, False)

    def test_RMSDformula(self):
        answer = 0

        model = np.array([[1,2,3],[2,3,4],[3,4,5]])
        target = np.array([[1,2,3],[2,3,4],[3,4,5]])
        lambda_max = functions.find_lambda_max(model, target)
        result = functions.RMSDformula(model, target,lambda_max)
        self.assertEqual(answer, result)

    def test_weightmatrix(self):
        answer = np.array([[-1.33333333,-1.33333333,-0.33333333],
                           [ 0.66666667, 0.66666667,-1.33333333],
                           [0.66666667,0.66666667,1.66666667]])
        matrix = np.array([[1,2,3],[3,4,2],[3,4,5]])
        result = functions.weightmatrix(matrix)
        self.assertEqual(answer, result)


if __name__ == '__main__':
    unittest.main()
