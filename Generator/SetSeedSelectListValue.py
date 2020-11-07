# Random Generator function #5
# Set a seed and randomly select the same value from a list
import random
from Validation import Validations


def set_seed_select_list_value(data):
    Validations.empty_list_check(data)
    Validations.check_for_valid_numbers(data)
    random.seed(8)
    return random.choice(data)
