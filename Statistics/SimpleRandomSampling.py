import random
from Validation.Validations import empty_list_check
from Validation.Validations import check_for_valid_numbers


def get_sample(data, sample_size):
    # Validations
    empty_list_check(data)
    check_for_valid_numbers(data)

    return random.sample(data, sample_size)
