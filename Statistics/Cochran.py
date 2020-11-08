from Calculator.Square import square
from Calculator.Multiplication import multiplication
from Calculator.Division import division
from Statistics.StandardDeviation import standard_deviation
from Statistics.MarginOfError import margin_of_error
from Validation.Validations import empty_list_check
from Validation.Validations import check_for_valid_numbers


def cochran(sample, confidence_interval, x):
    # Validations
    check_for_valid_numbers(sample)
    empty_list_check(sample)

    # Formula: (Z^2)(p)(q) / (e^2) -> https://www.statisticshowto.com/probability-and-statistics/find-sample-size/
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
    margin_of_error_result = square(margin_of_error(sample, x))
    return division(margin_of_error_result, multiplication(multiplication(square(z), 1.5), 1.5))
