from Calculator.Division import division
from Statistics.Mean import mean
import math


def median(data):
    data_len = len(data)
    data.sort()

    # data set has even number of elements
    if data_len % 2 == 0:

        # find middle
        mid = math.trunc(division(2, data_len))

        # find middle left value
        mid_left = data[mid - 1]

        # find middle right value
        mid_right = data[mid]

        list_of_items = []
        list_of_items.insert(0, mid_left)
        list_of_items.insert(1, mid_right)
        return mean(list_of_items)
    else:
        # data set has odd number of elements
        return data[round(division(2, data_len))]
