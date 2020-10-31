from Calculator.Division import division
from Calculator.Substraction import subtraction
from Calculator.Addition import addition
from Statistics.Mean import mean

def median(data):
    # TODO: sanitize data
    data_len = len(data)
    data.sort()

    # data set has even number of elements
    if data_len % 2 == 0:
        # find middle left value
        mid_left = data[division(2, data_len)]
        # find middle right value
        mid_right = data[division(subtraction(1, 2), data_len)]
        # return mean of middle left and middle right values
        return division(2, addition(mid_left, mid_right))
        # TODO: add after mean implementation
        #return mean(mid_left, mid_right)
    # data set has odd number of elements
    else:
        return data[division(2, data_len)]