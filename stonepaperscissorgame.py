import random

Choice = ["Rock", "Paper","Scissor"]
while True:
    print("Rock Paper Scissor Game:")
    Youwin, Computerwin = 0, 0
    for i in range(1, 6):
        print("Round", i, "Start:")
        print("Please select any one option:")
        print("1.Rock", "2.Paper", "3.Scissor", sep="\n")
        Yourchoice = int(input("Enter your choice:"))
        if Yourchoice == 1:
            print("You select Rock")
            Yourchoice = "Rock"
        elif Yourchoice == 2:
            print("You select Paper")
            Yourchoice = "Paper"
        elif Yourchoice == 3:
            print("You select Scissor")
            Yourchoice = "Scissor"
        else:
            print("lnvalid Choice")
            break
        Computerchoice = random.choice(Choice)  # Random select by computer using result and give the point
        print("Computer selected", Computerchoice)
        if Yourchoice == Computerchoice:
            Youwin += 1
            Computerwin += 1
            print("This round is Drawn")
        elif (Yourchoice == "Paper" and Computerchoice == "Rock") or (Yourchoice== "Rock" and Computerchoice == "Scissor") or (Yourchoice == "Scissor" and Computerchoice == "Paper"):
            Youwin += 1
            print("You win this Round")
        else:
            Computerwin += 1
            print("Computer wins this Round")
# if you have more point than computer then you win and vice versa
    if Youwin > Computerwin:
        print("You win the game:")
        print("Score is:", "Your score:", Youwin, " Computer score:", Computerwin, sep="\n")
    if Computerwin > Youwin:
        print("You lost the game and Computer wins this game:")
        print("Score is:", "Your score:", Youwin, " Computer score:", Computerwin, sep="\n")
    else:
        print("Match Drawn")
        print("Score is:", "Your score:", Youwin, " Computer score:", Computerwin, sep="\n")
    user_choice = input("Want to play again?(Yes/Exit)")
    if user_choice == 'yes' or user_choice == 'Yes' or user_choice == 'YES':
       continue
    else:
       break
