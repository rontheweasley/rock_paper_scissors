import random
import time

ai = "Robot"
playerChoice = 0
statics1 = 0
statics2 = 0

print("This is Rock, Paper, Scissors;\n1 - Rock\n2 - Paper\n3 - Scissors\n")
time.sleep(2)

while True:

    randomNumber = random.randrange(3)

    if randomNumber == 0:
        ai = "Rock"

    elif randomNumber == 1:
        ai = "Paper"

    elif randomNumber == 2:
        ai = "Scissors"

    print("Time is running out!")

    for x in (3, 2, 1):
        time.sleep(1)
        print(x,"...")
        time.sleep(1)

    playerChoice = int(input("\nI'm : "))

    if playerChoice == 1:
        player = "Rock"

    elif playerChoice == 2:
        player = "Paper"

    elif playerChoice == 3:
        player = "Scissors"

    elif playerChoice == 4:
        print("AI has won {} game.\nPlayer has won {} game.".format(statics1,statics2))
        break

    else:
        print("This is a mistake!")
        time.sleep(1)
        pass

    print("Player is",player)

    if ai == "Rock" and player == "Rock":
        print("AI is", ai)
        playerChoice = input("Tie!\nLet's play again!\nWill play? : ")
        if playerChoice != "yes":
            print("Ahaha LOSER!")
            break

    elif ai == "Rock" and player == "Paper":
        print("AI is", ai)
        playerChoice = input("Congrats, You won!\nLet's play again!\nWill play? : ")
        statics2 = statics2 + 1;
        if playerChoice != "yes":
            print("Ahaha LOSER!")
            break

    elif ai == "Rock" and player == "Scissors":
        print("AI is", ai)
        playerChoice = input("AI Won, Loser!\nDo you want play again?\nWill play? : ")
        statics1 = statics1 + 1;
        if playerChoice != "yes":
            print("Ahaha LOSER!")
            break


    elif ai == "Paper" and player == "Rock":
        print("AI is", ai)
        playerChoice = input("AI Won, Loser!\nDo you want play again?\nWill play? : ")
        statics1 = statics1 + 1;
        if playerChoice != "yes":
            print("Ahaha LOSER!")
            break

    elif ai == "Paper" and player == "Paper":
        print("AI is", ai)
        playerChoice = input("Tie!\nLet's play again!\nWill play? : ")
        if playerChoice != "yes":
            print("Ahaha LOSER!")
            break


    elif ai == "Paper" and player == "Scissors":
        print("AI is", ai)
        playerChoice = input("Congrats, You won!\nLet's play again!\nWill play? : ")
        statics2 = statics2 + 1;
        if playerChoice != "yes":
            print("Ahaha LOSER!")
            break


    elif ai == "Scissors" and player == "Rock":
        print("AI is", ai)
        playerChoice = input("Congrats, You won!\nLet's play again!\nWill play? : ")
        statics2 = statics2 + 1;
        if playerChoice != "yes":
            print("Ahaha LOSER!")
            break


    elif ai == "Scissors" and player == "Paper":
        print("AI is", ai)
        playerChoice = input("AI Won, Loser!\nDo you want play again?\nWill play? : ")
        statics1 = statics1 + 1;
        if playerChoice != "yes":
            print("Ahaha LOSER!")
            break


    elif ai == "Scissors" and player == "Scissors":
        print("AI is", ai)
        playerChoice = input("Tie!\nLet's play again!\nWill play? : ")
        if playerChoice != "yes":
            print("Ahaha LOSER!")
            break