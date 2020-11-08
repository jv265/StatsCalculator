from Calculator.Square import square
from Calculator.Substraction import subtraction
from Calculator.Addition import addition
from Calculator.Division import division
from Statistics.Mean import mean
import math
from Validation.Validations import empty_list_check
from Validation.Validations import check_for_valid_numbers


def variance(data):
    # Validations
    empty_list_check(data)
    check_for_valid_numbers(data)

    n = len(data)
    calculated_mean = mean(data)
    result = 0

    for x in data:
        result = addition(square(subtraction(calculated_mean, x)), result)
    return division(n, result)
