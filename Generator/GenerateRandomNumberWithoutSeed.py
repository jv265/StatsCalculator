from numpy.random import randint
import random


def generate_random_number_with_seed_for_int():
    return randint(0, 10)


def generate_random_number_with_seed_for_float():
    return random.uniform(0.0, 10.0)

