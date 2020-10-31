from Statistics.Mean import mean
from Statistics.StandardDeviation import standard_deviation
from Calculator.Division import division
from Calculator.Substraction import subtraction


def zscore(data, x):
    return division(standard_deviation(data), subtraction(mean(data), x))
