# Random Generator function #3
# Generate a list of N random numbers with a seed and between a range of numbers - Both Integer and Decimal
import random

random.seed(7)


def n_random_ints(n):
    return random.sample(range(1, 11), n)


def n_random_floats(n):
    random_floats = []
    for i in range(0, n):
        x = round(random.uniform(1.0, 10.0), 2)
        random_floats.append(x)
    return random_floats
