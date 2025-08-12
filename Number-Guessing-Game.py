import random

class Number_guess_game:
    def __init__(self):
        self.secret_number = random.randint(1,100)
        self.number_guess =0
    def play(self):

        self.number_guess = int(input("Enter your guess :"))
        if self.number_guess == self.secret_number:
            print(f"You guessed right. Number was {self.secret_number} \n")
        elif self.number_guess > self.secret_number:
            print(f"Your guess was big. Number was {self.secret_number}")
        else:
            print(f"Your guess was smaller. Number was {self.secret_number}")


game = Number_guess_game()
game.play()