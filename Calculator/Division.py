from Validation import Validations


def division(a, b):
    Validations.divide_by_zero_check(a)
    return float(b) / float(a)
