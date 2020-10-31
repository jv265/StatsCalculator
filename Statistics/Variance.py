from Calculator.Addition import addition
from Calculator.Square import square
from Calculator.Division import division
from Calculator.Substraction import subtraction
from Statistics.Mean import mean

def variance(data):
    n = len(data)
    sum = 0
    for i in range(n):
        sum = addition(sum, square(data[i]))
    var = subtraction(division(n, sum), square(mean(data)))
    return var