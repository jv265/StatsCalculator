from Statistics.StandardDeviation import standard_deviation
from Calculator.Multiplication import multiplication
from Calculator.Division import division
from Calculator.SquareRoot import square_root
from Validation.Validations import empty_list_check
from Validation.Validations import check_for_valid_numbers
from Statistics import CalculateZValue


def margin_of_error(sample, confidence_level):
    # Validations
    empty_list_check(sample)
    check_for_valid_numbers(sample)

    z = CalculateZValue.calculate_zvalue(confidence_level)
    sample_size = len(sample)
    standard_deviation_result = standard_deviation(sample)
    return multiplication(z, division(square_root(sample_size), standard_deviation_result))
