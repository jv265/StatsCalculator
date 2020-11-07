from Calculator.Square import square
from Calculator.Substraction import subtraction
from Statistics.Mean import mean
import math


def variance(data):
    n = len(data)
    calculated_mean = math.floor(mean(data))
    calculated_list = []

    for i in range(n):
        calculated_list.insert(i, square(subtraction(calculated_mean, data[i])))
    return mean(calculated_list)
