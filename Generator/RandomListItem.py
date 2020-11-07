# Random Generator function #4
# Select a random item from a list
import random
from Validation import Validations


def random_list_item(data):
    Validations.empty_list_check(data)
    Validations.check_for_valid_numbers(data)
    return random.choice(data)
