from Statistics.StandardDeviation import standard_deviation
from Statistics.ZScore import zscore
from Calculator.Multiplication import multiplication
from Calculator.Division import division
from Calculator.SquareRoot import square_root


def margin_of_error(sample, x):
    zscore_result = zscore(sample, x)
    sample_size = len(sample)
    standard_deviation_result = standard_deviation(sample)
    return multiplication(zscore_result, division(square_root(sample_size), standard_deviation_result))
