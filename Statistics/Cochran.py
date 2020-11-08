from Calculator.Square import square
from Calculator.Multiplication import multiplication
from Calculator.Division import division
from Statistics.MarginOfError import margin_of_error
from Validation.Validations import empty_list_check
from Validation.Validations import check_for_valid_numbers
from Statistics import CalculateZValue


def cochran(sample, confidence_level, x):
    # Validations
    check_for_valid_numbers(sample)
    empty_list_check(sample)

    # Formula: (Z^2)(p)(q) / (e^2) -> https://www.statisticshowto.com/probability-and-statistics/find-sample-size/
    # Assuming p is 0.5

    # calculate z from a given confidence interval
    z = CalculateZValue.calculate_zvalue(confidence_level)

    margin_of_error_result = square(margin_of_error(sample, x))
    return division(margin_of_error_result, multiplication(multiplication(square(z), 0.5), 0.5))
