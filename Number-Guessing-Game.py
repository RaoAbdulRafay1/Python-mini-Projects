import random

class Number_guess_game:
    def __init__(self):
        self.secret_number = random.randint(1,100)
        self.number_guess =0
        