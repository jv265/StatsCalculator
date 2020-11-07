from Statistics.StandardDeviation import standard_deviation
from Calculator.Multiplication import multiplication
from Calculator.Division import division
from Calculator.SquareRoot import square_root
from Validation.Validations import empty_list_check
from Validation.Validations import check_for_valid_numbers


def margin_of_error(sample, confidence_level):
    # Validations
    empty_list_check(sample)
    check_for_valid_numbers(sample)

    # Source: https://www.surveymonkey.com/mp/margin-of-error-calculator/
    # First find our Z value from a confidence level
    if confidence_level == 80:
        z = 1.645
    elif confidence_level == 85:
        z = 1.645
    elif confidence_level == 90:
        z = 1.645
    elif confidence_level == 95:
        z = 1.96
    elif confidence_level == 98:
        z = 2.33
    elif confidence_level == 99:
        z = 2.58
    else:
        return 0

    sample_size = len(sample)
    standard_deviation_result = standard_deviation(sample)
    return multiplication(z, division(square_root(sample_size), standard_deviation_result))
