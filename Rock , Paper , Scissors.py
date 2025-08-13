import random
def get_choices():
    player_choice=input("Enter choice (rock,paper,scissors) :")
    options=["rock","paper","scissors"]
    computer_choice=random.choice(options)
    choice={"player":player_choice ,"computer":computer_choice}
    return choice
def check_win(player,computer):
    print(f"You choose {player} ,Computer choose {computer}")
    if player==computer:
        return "It's a tie"
    elif player=="rock":
        if computer=="scissors":
            return "You win"
        else:
            return "You lose"
    elif player=="paper":
        if computer=="scissors":
            return "You lose"
        else:
            return "You win"
    elif player=="scissors":
        if computer=="paper":
            return "You win"
        else:
            return "You lose"                  
choice=get_choices()
p_choice=choice["player"]
c_choice=choice["computer"]

result=check_win(p_choice,c_choice)
print(result)
def play_again():
    again = input("Do you want to play again? (yes/no): ").lower()
    if again == 'yes':
        choice = get_choices()
        p_choice = choice["player"]
        c_choice = choice["computer"]
        result = check_win(p_choice, c_choice)
        print(result)
        play_again()
    else:
        print("Thanks for playing!")
play_again()

