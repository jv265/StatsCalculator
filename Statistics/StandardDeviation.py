from Calculator.SquareRoot import square_root
from Statistics.Variance import variance
from Validation.Validations import empty_list_check
from Validation.Validations import check_for_valid_numbers


def standard_deviation(data):
    # Validations
    empty_list_check(data)
    check_for_valid_numbers(data)

    return square_root(variance(data))
