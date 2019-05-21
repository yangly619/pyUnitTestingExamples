
import unittest

from Factorial import Factorial


class TestMethods(unittest.TestCase):

    def setUp(self):
        self.factorial = Factorial()

    def test_should_factorial_of_zero_return_one(self):
        self.assertEqual(1, self.factorial.compute(0))

    def test_should_factorial_of_one_return_one(self):
        self.assertEqual(1, self.factorial.compute(1))

    def test_should_factorial_of_two_return_two(self):
        self.assertEqual(2, self.factorial.compute(2))

    def test_should_factorial_of_three_return_six(self):
        self.assertEqual(6, self.factorial.compute(3))

    def test_should_factorial_of_three_return_six(self):
        self.assertEqual(6, self.factorial.compute(3))

    def test_should_factorial_of_a_negative_number_raise_an_exception(self):
        self.assertRaises(Exception, self.factorial.compute, -1)

    def test_should_factorial_of_a_negative_number_raise_an_exception_v2(self):
        with self.assertRaises(Exception):
            self.factorial.compute(-1)

    def test_should_factorial_of_five_return_120(self):
        self.assertEqual(120, self.factorial.compute(5))
