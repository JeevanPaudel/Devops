mport random

def game():
    user = input("Choose 's' for SCISSOR, 'p' for PAPER,'r' for ROCK :")
    print("Welcome to the game (Version: z)")
    comp = random.choice(('s', 'p', 'r'))

    if user == comp:
        print("It's a tie !!")

    elif win(user, comp):                          #Game theory s>p,r>s,p>r
        print("You Won!!")
    else:
        print("Computer won")


def win(user, comp):
    #wins when s>p,r>s,p>r
    if (user =='s' and comp == 'p') or (user =='r' and comp == 's') or (user =='p' and comp == 'r'):
        return True                      #True is returned if player wins

game()

