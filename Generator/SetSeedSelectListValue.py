# Random Generator function #5
# Set a seed and randomly select the same value from a list
import random

def set_seed_select_list_value(data):
    random.seed(8)
    return random.choice(data)
