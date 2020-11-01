from numpy.random import randint


# Random Generator Function 6
# Select N number of items from a list without a seed

def select_n_numbers_without_seed(n):
    list_of_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n_numbers = []
    for i in range(n):
        n_numbers[i] = list_of_numbers[randint(0, 10)]
    return n_numbers

