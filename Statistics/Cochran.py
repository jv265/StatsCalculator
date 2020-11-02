from Calculator.Square import square
from Calculator.Multiplication import multiplication
from Calculator.Division import division
from Statistics.StandardDeviation import standard_deviation
from Statistics.MarginOfError import margin_of_error


def cochran(sample, confidence_interval, x):

    # n (sample size calculation) = (z ^2 * sd) / moe
    # calculate z from a given confidence interval
    # 90 % -> 1.645
    # 95 % -> 1.96
    # 98 & -> 2.33
    # 99 % -> 2.575
    # source: https://www.youtube.com/watch?v=sJyZ9vRhP7o

    if confidence_interval == 90:
        z = 1.645
    elif confidence_interval == 95:
        z = 1.96
    elif confidence_interval == 98:
        z = 2.33
    elif confidence_interval == 99:
        z = 2.575
    else:
        return 0
    margin_of_error_result = margin_of_error(sample, x)
    return division(margin_of_error_result, multiplication(square(z), standard_deviation(sample)))
