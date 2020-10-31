from Calculator.SquareRoot import square_root
from Statistics.Variance import variance


def standard_deviation(data):
    return square_root(variance(data))
