from numpy.random import randint
from numpy.random import seed
import random


# Random Generator Function 2
# Generate a random number with a seed between a range of two numbers - Both Integer and Decimal

def generate_random_number_with_seed_for_int():
    seed(5)
    return randint(0, 10)


def generate_random_number_with_seed_for_float():
    seed(5)
    return random.uniform(0.0, 10.0)

