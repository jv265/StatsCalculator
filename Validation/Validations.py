def divide_by_zero_check(x):
    if x == 0:
        raise Exception("Cannot divide by zero.")


def empty_list_check(sample):
    if len(sample) == 0:
        raise Exception("The List is Empty.")


def check_for_valid_numbers(sample):
    for i in range(len(sample)):
        if isinstance(sample[i], str):
            raise Exception("The list does not contain valid numbers.")
