#Rock Paper Scissors game
#Computer vs User
#import random module
import random
while True:
    print("Rock Paper Scissors")
    #Game Rules
    print("Game Rules Winning Rules\nRock vs Paper--> Paper Wins\nRock vs Scissor--> Rock Wins\nPaper vs Scissor--> Scissor Wins")
    print('Select = 1.Rock, 2.Paper, 3.Scissor\n')
    print("==> User Turn <==\n")
    #User turn
    #select one from 1.Rock,2. Paper,3.Scissor
    user=int(input("enter your choice: "))
    #condition for user input
    #conditions based on the user input
    if user==1:
        print("user choice is 'Rock'\n")
    elif user==2:
        print("user choice is 'Paper'\n")
    else :
        print("user choice is 'Scissor'\n")
    #Computers Turn
    print("==> Now computer's Turn <==\n")
    #randomly selects one number from 1,2,3
    comp=random.randint(1,3)
    #if computer & user input is same
    if comp==user:
        comp=random.randint(1,3)
    #conditions based on the computer input
    if comp==1:
        print("computer choice is 'Rock'")
    elif comp==2:
        print("comp choice is 'Paper'")
    else :
        print("comp choice is 'Scissor'")
    #incase of Draw
    if comp==user:
        print("its a Draw\n==> the game is tie <==")
    #Rock vs Paper
    if comp==1 and user==2:
        print("Rock vs Paper-->Paper Wins\n...................\n==> User Wins <==\n....................")
    #Paper vs Rock
    elif comp==2 and user==1:
        print("Paper vs Rock-->Paper Wins\n....................\n==> Computer Wins <==\n...................")
    #Paper vs Scissor
    if comp==2 and user==3:
        print("Paper vs Scissor-->Scissor Wins\n...................\n==> User Wins <==\n.....................")
    #Scissor vs Paper
    elif comp==3 and user==2:
        print("Scissor vs Paper-->Scissor Wins\n....................\n==> Computer Wins <==\n.................")
    #Rock vs Scissor
    if comp==1 and user==3:
        print("Rock vs Scissor-->Rock Wins\n.........................\n==> Computer Wins <==\n....................")
    #Scissor vs Rock
    elif comp==3 and user==1:
        print("Scissor vs Rock-->Rock Wins\n.........................\n==> User Wins <==\n......................")
    print("want to play again(y/n)")
    ans=input().lower()
    if ans=="n":
        break
print("Thanks for Playing")
    

        




    









    




    



