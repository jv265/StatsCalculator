from Statistics.Mean import mean
from Statistics.StandardDeviation import standard_deviation
from Calculator.Division import division
from Calculator.Substraction import subtraction
from Validation.Validations import empty_list_check
from Validation.Validations import check_for_valid_numbers


# X is the raw score
def zscore(data, x):
    # Validations
    empty_list_check(data)
    check_for_valid_numbers(data)

    return division(standard_deviation(data), subtraction(mean(data), x))
