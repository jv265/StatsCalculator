from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.Median import median
from Statistics.Mode import mode
from Statistics.StandardDeviation import standard_deviation
from Statistics.Variance import variance
from Statistics.ZScore import zscore
from Statistics.MarginOfError import margin_of_error
from Statistics.Cochran import cochran
from Statistics.SampleSizeUnkownPop import sample_size_unknown_pop
from Statistics.ConfidenceInterval import confidence_interval
from Statistics.SimpleRandomSampling import get_sample


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

    def margin_of_error(self, sample, confidence_level):
        self.result = margin_of_error(sample, confidence_level)
        return self.result

    def cochran(self, sample, confidence_level):
        self.result = cochran(sample, confidence_level)
        return self.result

    def sample_size_unknown_population(self, confidence_level, width):
        self.result = sample_size_unknown_pop(confidence_level, width)
        return self.result

    def confidence_interval(self, sample, confidence_level):
        self.result = confidence_interval(sample, confidence_level)
        return self.result

    def simple_random_sampling(self, sample, sample_size):
        self.result = get_sample(sample, sample_size)
        return self.result
