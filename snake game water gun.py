# import random
# SWG = ["Snake", "Water", "Gun"]
# computer = random.choice(SWG)
# player = False
# i = 0
# Pscr = 0
# Cscr = 0
# '''Player False rakha Kyon Ki Jab program run hoga tab
# status change hoke from False to True ho jayega
# kyon ki jab hi player ko koi value dunga uski status true ho jayegi'''
# while (i<10):
#     player = input("Snake, Water, Gun?")
#     if player == computer:
#         print("Tie!")
#     elif player == "Snake":
#         if computer == "Gun":
#             print("You lose!", computer, "Maar Diya", player, "Ko.")
#             Pscr = Pscr-1
#             Cscr = Cscr+1
#         else:
#             print("You win!", player, "Bhag Gaya Swim Karke", computer, "Mein." )
#             Pscr = Pscr + 1
#             Cscr = Cscr - 1
#     elif player == "Water":
#         if computer == "Snake":
#             print("You lose!", computer, "Bhag Gaya Swim Karke", player, "Mein." )
#             Pscr = Pscr - 1
#             Cscr = Cscr + 1
#         else:
#             print("You win!", player, "Duba Diya", computer, "Ko." )
#             Pscr = Pscr + 1
#             Cscr = Cscr - 1
#     elif player == "Gun":
#         if computer == "Water":
#             print("You lose...", computer, "Bhigo Diya", player, "Ko.")
#             Pscr = Pscr - 1
#             Cscr = Cscr + 1
#         else:
#             print("You win!", player, "Maar Diya", computer, "Ko.")
#             Pscr = Pscr + 1
#             Cscr = Cscr - 1
#     else:
#         print("Check your spelling!")
#     computer = random.choice(SWG)
#     i= i+1
#     if (i==5):
#         try:
#             Pscr < 0
#             Cscr < 0
#             print("Your Final Score Is", Pscr)
#             print("And Computers Final Score Is", Cscr)
#         except Exception as e:
#
#                  print("Your Final Score Is",Pscr)
#         print("And Computers Final Score Is",Cscr)
#
#         if Pscr == Cscr:
#             print("Match Drawn")
#         elif Pscr>Cscr:
#             print('You Win')
#
#         else:
#             print("You Lose")

# import random
# dict = {"1":"Snake","2":"Water","3":"Gun"}
# snake = list (dict.keys())[0]
# water = list (dict.keys())[1]
# gun = list (dict.keys())[2]
# turns = int(input("How many games do you want to play?: "))
# gamesCount = 0
# comp = []
# user = []
# choice = ""
# while turns>0:
#     gamesCount += 1
#     compTurn = random.choice(list(dict.keys()))
#     while choice not in list (dict.keys()):
#         print(f"Games No. {gamesCount}")
#         print("------------")
#         for key, value in dict.items():
#             print(f"Select {key} for {value}: ")
#         choice = input()
#         userTurn = choice
#         if(choice not in list(dict.keys())):
#             print("Incorrect option selected. Try again...!!!")
#     choice=""
#     if compTurn == snake:
#         if userTurn == water:
#             print(f"Computer won. Computer selected {dict[compTurn]} and you selected {dict[userTurn]}")
#             comp.append(f"Won [{dict[compTurn]}]")
#             user.append(f"Lost [{dict[userTurn]}]")
#         elif userTurn == gun:
#             print(f"You won. Computer selected {dict[compTurn]} and you selected {dict[userTurn]}")
#             comp.append(f"Lost [{dict[compTurn]}]")
#             user.append(f"Won [{dict[userTurn]}]")
#         elif userTurn == snake:
#             print(f"Match Tied. Computer selected {dict[compTurn]} and you also selected {dict[userTurn]}")
#             comp.append(f"Tied [{dict[compTurn]}]")
#             user.append(f"Tied [{dict[userTurn]}]")
#     elif compTurn == water:
#         if userTurn == gun:
#             print(f"Computer won. Computer selected {dict[compTurn]} and you selected {dict[userTurn]}")
#             comp.append(f"Won [{dict[compTurn]}]")
#             user.append(f"Lost [{dict[userTurn]}]")
#         elif userTurn == snake:
#             print(f"You won. Computer selected {dict[compTurn]} and you selected {dict[userTurn]}")
#             comp.append(f"Lost [{dict[compTurn]}]")
#             user.append(f"Won [{dict[userTurn]}]")
#         elif userTurn == water:
#             print(f"Match Tied. Computer selected {dict[compTurn]} and you also selected {dict[userTurn]}")
#             comp.append(f"Tied [{dict[compTurn]}]")
#             user.append(f"Tied [{dict[userTurn]}]")
#     elif compTurn == gun:
#         if userTurn == snake:
#             print(f"Computer won. Computer selected {dict[compTurn]} and you selected {dict[userTurn]}")
#             comp.append(f"Won [{dict[compTurn]}]")
#             user.append(f"Lost [{dict[userTurn]}]")
#         elif userTurn == water:
#             print(f"You won. Computer selected {dict[compTurn]} and you selected {dict[userTurn]}")
#             comp.append(f"Lost [{dict[compTurn]}]")
#             user.append(f"Won [{dict[userTurn]}]")
#         elif userTurn == gun:
#             print(f"Match Tied. Computer selected {dict[compTurn]} and you also selected {dict[userTurn]}")
#             comp.append(f"Tied [{dict[compTurn]}]")
#             user.append(f"Tied [{dict[userTurn]}]")
#     turns -= 1
#     if(turns == 0):
#         compWinCount = sum("Won" in s for s in comp)
#         userWinCount = sum("Won" in s for s in user)
#         print("\n################################################################################")
#         print("Game No    Computer Result       Your Result")
#         print("---------------------------------------------")
#         for index in range(len(comp)):
#             # print(item1, end = ", ")
#             print(f"    {index + 1}      {comp[index]}       {user[index]}")
#         if compWinCount > userWinCount:
#             print(f'''
# Final Result
# ******************************************************************************
# Bad Luck! Computer is the Winner. Computor won {compWinCount} game(s) and you won {userWinCount} game(s)...!!!
# Better Luck next time...!!!
# ********************************************************************************''')
#         elif compWinCount < userWinCount:
#             print(f'''
# Final Result
# *************************************************************************
# Congratulations!You are the Winner. Computor won {compWinCount} game(s) and you won {userWinCount} game(s)...!!!
# ***************************************************************************''')
#         else:
#             print(f'''
# Final Result
# *********************************************
# Match tied. Both won {compWinCount} game(s)...!!!
# ***********************************************''')
#         while True:
#             playAgain = input("\nDo you want to play again? (Y/N): ")
#             if playAgain.upper() == "Y":
#                 turns = int(input("\nHow many games do you want to play?: "))
#                 gamesCount = 0
#                 comp = []
#                 user = []
#                 break
#             elif playAgain.upper() == "N":
#                 print("Thanks for playing...!!!")
#                 break
#             else:
#                 print("Value should be either Y or N. Try again...!!!")
#                 continue
#     continue


import random
name=input("Please Enter your name: ")
n=0 #counter for number of games
cu=0#counter for wins of user
cp=0#counter for wins of computer
while n<5:
    choose=input("Please type your choice:\n"
               "1.Rock\n2.Paper\n3.Scissor\n")
    L=["Rock","Paper","Scissor"]
    comp=random.choice(L)
    if choose == "Rock":
        if comp == choose:
            print(f"Match is draw::{choose} vs {comp} ")
        elif comp == "Scissor":
            print(f"You won ::{choose} vs {comp}")
            cu+=1
        elif comp == "Paper":
            print(f"You Lost ::{choose} vs {comp}")
            cp+=1
    if choose == "Paper":
        if comp == choose:
            print(f"Match is draw::{choose} vs {comp} ")
        elif comp == "Scissor":
            print(f"You Lost ::{choose} vs {comp}")
            cp+=1
        elif comp == "Rock":
            print(f"You Won ::{choose} vs {comp}")
            cu+=1
    if choose == "Scissor":
        if comp == choose:
            print(f"Match is draw::{choose} vs {comp} ")
        elif comp == "Paper":
            print(f"You won ::{choose} vs {comp}")
            cu+=1
        elif comp == "Rock":
            print(f"You Lost ::{choose} vs {comp}")
            cp+=1
    n+=1
print(f"the matches win by you are '{cu}' and computer are {cp}")
if(cu>cp):
    print(f"\n{name} is the Winner".upper())
else:
    print("\nSorry Computer is a winner".upper())