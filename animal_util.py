
from random import choice

meals = ["fish", "chicken","steak"]

def choose_random_meal():
    if not meals:
        return None  # Handle empty list case
    else:
        return choice(meals)
