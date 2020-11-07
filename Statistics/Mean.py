from Calculator.Addition import addition
from Calculator.Division import division
from Validation.Validations import empty_list_check
from Validation.Validations import check_for_valid_numbers


def mean(data):
    # Validations
    empty_list_check(data)
    check_for_valid_numbers(data)

    num_values = len(data)
    total = 0

    for num in data:
        total = addition(total, num)
    return division(num_values, total)
