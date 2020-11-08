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
        try:
            mode = self.statistics.mode(self.testData)
        except:
            print("No Mode Found")
            return
        self.assertEqual(mode, statistics.mode(self.testData))

    def test_median_calculator(self):
        median = self.statistics.median(self.testData)
        self.assertEqual(median, statistics.median(self.testData))

    def test_variance_calculator(self):
        variance = self.statistics.variance(self.testData2)
        self.assertEqual(round(variance, 2), round(statistics.pvariance(self.testData2), 2))

    def test_zscore_calculator(self):
        zscore = self.statistics.zscore(self.testData2, 9)
        self.assertEqual(round(zscore, 2), -0.97)

    def test_standard_deviation_calculator(self):
        standard_deviation = self.statistics.standard_deviation(self.testData)
        self.assertEqual(round(standard_deviation), round(statistics.stdev(self.testData)))

    def test_confidence_interval_calculator(self):
        # define sample, confidence interval
        confidence_interval = self.statistics.confidence_interval(self.testData2, 95)
        self.assertEqual(round(confidence_interval, 0), 44)

    def test_simple_random_sampling_calculator(self):
        # define sample, size
        random_sample = self.statistics.simple_random_sampling(self.testData2, 11)
        self.assertEqual(len(random_sample), 11)

    def test_sample_size_unknown_population_calculator(self):
        # define confidence level, width
        # reference: https://www.statisticshowto.com/probability-and-statistics/find-sample-size/
        sample_size = self.statistics.sample_size_unknown_population(95, 0.06)
        self.assertEqual(sample_size, 1067.11)

    def test_cochran_calculator(self):
        cochran = self.statistics.cochran(self.testData2, 80)
        self.assertEqual(round(cochran, 2), 0.01)

    def test_margin_of_error_calculator(self):
        margin_of_error = self.statistics.margin_of_error(self.testData2, 95)
        self.assertEqual(round(margin_of_error, 2), 10.96)


if __name__ == '__main__':
    unittest.main()
