import random

class Number_guess_game:
    def __init__(self):
        self.secret_number = random.randint(1,100)
        self.difficulty ="easy"
        self.number_guess = 0
    def play(self,diff):
        attempts = 0
        self.difficulty = diff
        Out ="no"
        if self.difficulty == "easy":
            attempts = 15
        elif self.difficulty == "medium":
            attempts = 10
        elif self.difficulty == "hard":
            attempts = 5
        else:
            print("Wrong difficulty\n")
            attempts = 0            

        while attempts != 0:

            self.number_guess = int(input("Enter your guess :"))
            attempts -=1

            if self.number_guess == self.secret_number:
                print(f"You guessed right. Number was {self.secret_number} \n")
                return 
            elif self.number_guess > self.secret_number:
                print(f"Your guess was big. Enter NO/N to quit")
                Out = input().upper()
            else:
                print(f"Your guess was smaller.Enter  NO/N to quit")
                Out = input().upper()
            if Out == "NO" or Out == "N":
                break

            
        print(f"You lost. Number was {self.secret_number}")        


game = Number_guess_game()
print("****************Welcome to Number Guessing Game***************")
print("****You have to guess a number between 1 and 100****")
print("****You can quit the game at any time by entering NO/N****")
print("****Choose difficulty level****")
print("Enter difficulty easy/medium/hard :")
diff = input().lower()
game.play(diff)
