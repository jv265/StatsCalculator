# automation test
import unittest
import math

from Calculator.Calculator import Calculator
from CsvReader.CsvReader import CsvReader
from pprint import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        self.assertEqual(self.calculator.add(2, 2), 4)
        self.assertEqual(self.calculator.result, 4)

    def test_subtract_method_calculator(self):
        self.assertEqual(self.calculator.subtract(2, 2), 0)
        self.assertEqual(self.calculator.result, 0)

    def test_multiply_method_calculator(self):
        self.assertEqual(self.calculator.multiply(2, 2), 4)
        self.assertEqual(self.calculator.result, 4)

    def test_divide_method_calculator(self):
        self.assertEqual(self.calculator.divide(5, 10), 2)
        self.assertEqual(self.calculator.result, 2)

    def test_square_method_calculator(self):
        self.assertEqual(self.calculator.square(5), 25)
        self.assertEqual(self.calculator.result, 25)

    def test_square_root_method_calculator(self):
        self.assertEqual(self.calculator.square_root(49), 7)
        self.assertEqual(self.calculator.result, 7)

    # Unit tests testing individual csv files

    def test_subtraction(self):
        test_data_subtract = CsvReader('./Tests/Data/Unit Test Subtraction.csv').data
        for row in test_data_subtract:
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_addition(self):
        test_data_add = CsvReader('./Tests/Data/Unit Test Addition.csv').data
        for row in test_data_add:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_multiplication(self):
        test_data_multiply = CsvReader('./Tests/Data/Unit Test Multiplication.csv').data
        for row in test_data_multiply:
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_division(self):
        test_data_divide = CsvReader('./Tests/Data/Unit Test Division.csv').data
        for row in test_data_divide:
            self.assertEqual(self.calculator.divide(row['Value 1'], row['Value 2']), round(float(row['Result']), 9))
            self.assertEqual(self.calculator.result, round(float(row['Result']), 9))

    def test_square(self):
        test_data_square = CsvReader('./Tests/Data/Unit Test Square.csv').data
        for row in test_data_square:
            self.assertEqual(self.calculator.square(row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_square_root(self):
        test_data_square_root = CsvReader('./Tests/Data/Unit Test Square Root.csv').data
        for row in test_data_square_root:
            self.assertEqual(self.calculator.square_root(row['Value 1']), round(float(row['Result']), 8))
            self.assertEqual(self.calculator.result, round(float(row['Result']), 8))


if __name__ == '__main__':
    unittest.main()
