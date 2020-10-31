from Statistics.Mean import mean
from Statistics.StandardDeviation import standard_deviation
from Calculator.SquareRoot import square_root
from Calculator.Division import division
from Calculator.Multiplication import multiplication
from Calculator.Addition import addition


def confidence_interval(sample, confidence_level):
    z = confidence_level
    n = len(sample)
    s = standard_deviation(sample)
    x = mean(sample)
    return addition(x, multiplication(z, division(square_root(n), s)))
