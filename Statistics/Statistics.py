from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.Mode import mode
from Statistics.StandardDeviation import standard_deviation


class Statistics(Calculator):

    def mean(self, data):
        self.result = mean(data)
        return self.result

    def mode(self, data):
        self.result = mode(data)
        return self.result

    def standard_deviation(self, data):
        self.result = standard_deviation(data)
        return self.result
