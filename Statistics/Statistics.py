from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.Median import median
from Statistics.Mode import mode
from Statistics.StandardDeviation import standard_deviation
from Statistics.Variance import variance
from Statistics.ZScore import zscore


class Statistics(Calculator):

    def mean(self, data):
        self.result = mean(data)
        return self.result

    def median(self, data):
        self.result = median(data)
        return self.result

    def mode(self, data):
        self.result = mode(data)
        return self.result

    def standard_deviation(self, data):
        self.result = standard_deviation(data)
        return self.result

    def variance(self, data):
        self.result = variance(data)
        return self.result

    def zscore(self, data, x):
        self.result = zscore(data, x)
        return self.result
