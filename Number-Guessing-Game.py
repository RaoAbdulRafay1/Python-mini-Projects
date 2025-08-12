import random

class Number_guess_game:
    def __init__(self):
        self.secret_number = random.randint(1,100)
        self.number_guess =0
    def play(self):
        keep_playing = "yes"
        while keep_playing == "yes" or keep_playing == "YES" or keep_playing == "Y" or keep_playing == "y":

            self.number_guess = int(input("Enter your guess :"))
            if self.number_guess == self.secret_number:
                print(f"You guessed right. Number was {self.secret_number} \n")
                return 
            elif self.number_guess > self.secret_number:
                print(f"Your guess was big.Do you want to keep playing? ")
                keep_playing = input(" Then enter (yes/y)")

            else:
                print(f"Your guess was smaller.Do you want to keep playing? ")
                keep_playing = input("Then enter (yes/y)")
        print(f"You lost. Number was {self.secret_number}")        


game = Number_guess_game()
game.play()