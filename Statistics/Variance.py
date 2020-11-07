from Calculator.Square import square
from Calculator.Substraction import subtraction
from Statistics.Mean import mean
import math
from Validation.Validations import empty_list_check
from Validation.Validations import check_for_valid_numbers


def variance(data):
    # Validations
    empty_list_check(data)
    check_for_valid_numbers(data)

    n = len(data)
    calculated_mean = math.floor(mean(data))
    calculated_list = []

    for i in range(n):
        calculated_list.insert(i, square(subtraction(calculated_mean, data[i])))
    return mean(calculated_list)
