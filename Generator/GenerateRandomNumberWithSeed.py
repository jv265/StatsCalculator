from numpy.random import randint
from numpy.random import seed
import random


def generate_random_number_with_seed_for_int():
    seed(5)
    return randint(0, 10)


def generate_random_number_with_seed_for_float():
    seed(5)
    return random.uniform(0.0, 10.0)

