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
        mid_left = data[division(data_len, 2)]
        # find middle right value
        mid_right = data[division(data_len, subtraction(2, 1))]
        # return mean of middle left and middle right values
        return division(addition(mid_left, mid_right), 2)
        # TODO: add after mean implementation
        #return mean(mid_left, mid_right)
    # data set has odd number of elements
    else:
        return data[division(data_len, 2)]