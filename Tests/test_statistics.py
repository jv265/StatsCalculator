import unittest
from numpy.random import seed

from CsvReader.CsvReader import CsvReader
from Statistics.Statistics import Statistics
import random
import math
import statistics
import numpy as np


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.testData = np.random.choice(10, 20)
        self.testData2 = [1, 5, 9, 15, 22, 30, 40, 50, 44, 30, 20, 22, 32, 44, 55, 99, 90, 11, 22, 23]
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_calculator(self):
        mean = math.floor(self.statistics.mean(self.testData))
        self.assertEqual(mean, statistics.mean(self.testData))

    def test_mode_calculator(self):
        mode = self.statistics.mode(self.testData)
        self.assertEqual(mode, statistics.mode(self.testData))

    def test_median_calculator(self):
        median = self.statistics.median(self.testData)
        self.assertEqual(median, statistics.median(self.testData))

    def test_variance_calculator(self):
        variance = self.statistics.variance(self.testData)
        self.assertEqual(math.floor(variance), statistics.variance(self.testData))

    def test_zscore_calculator(self):
        zscore = self.statistics.zscore(self.testData2, 9)
        self.assertEqual(round(zscore, 2), -0.94)

    def test_standard_deviation_calculator(self):
        standard_deviation = self.statistics.standard_deviation(self.testData)
        self.assertEqual(round(standard_deviation), round(statistics.stdev(self.testData)))


if __name__ == '__main__':
    unittest.main()
