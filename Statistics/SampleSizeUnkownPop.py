from Calculator.Division import division
from Calculator.Multiplication import multiplication
from Calculator.Square import square
from Statistics.CalculateZValue import calculate_zvalue


def sample_size_unknown_pop(confidence_interval, width):
    p = 0.5
    q = 1 - p
    return multiplication(square(division(division(2, width), calculate_zvalue(confidence_interval))),
                          multiplication(p, q))
