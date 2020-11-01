from numpy.random import randint
from numpy.random import seed


# Random Generator Function 7
# Select N number of items from a list with a seed

def select_n_numbers_with_seed(n):
    list_of_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n_numbers = []
    for i in n:
        seed(5)
        n_numbers[i] = list_of_numbers[randint(0, 10)]
    return n_numbers

