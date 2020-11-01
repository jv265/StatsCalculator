from numpy.random import randint
import random


# Random Generator Function 1
# Generate a random number without a seed between a range of two numbers - Both Integer and Decimal

def generate_random_number_with_seed_for_int():
    return randint(0, 10)


def generate_random_number_with_seed_for_float():
    return random.uniform(0.0, 10.0)

