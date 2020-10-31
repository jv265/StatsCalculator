from numpy.random import randint


def select_n_numbers_without_seed_for_int(n):
    list_of_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n_numbers = []
    for i in range(n):
        n_numbers[i] = list_of_numbers[randint(0, 10)]
    return n_numbers


def select_n_numbers_without_seed_for_float(n):
    list_of_numbers = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
    n_numbers = []
    for i in range(n):
        n_numbers[i] = list_of_numbers[randint(0, 10)]
    return n_numbers
