# generate the random integer number a and b guess the numbers: you and your friend have to guess a number a and b. a and b are inputs taken by the user
# your friend is player 1n and plays first, he will have to keep choosing the number and your program must tell weather the number is greater
# than the actual number. log the number of trials it took your friend to arrive at the number . you play the same game then person with minimum of trials wins
#
# randomly generate tge number abf don't show the number to the user(say 6)
# input:
# enter the number a : 4
# enter the number b : 13
#
# output:
# player1:
# please guess the number between 4 and 13
# 5
# wrong guess a greater number again
# 8
# wring guess the smaller number again
# 6
# correct you took 3 trials to guess the numbers
# player2:
# .
# .
# .
# correct you took 7 trials to guess the number
# you win

import random
# p1=input("Enter the player name: ")
# p2=input("Enter the player name: ")
# choice=input(f"Enter the player which you want to be {p1} and {p2}: ")
# while choice == p1 or choice == p2:
#     # if choice==p1:
#      while True:
#         a = int(input("enter the value of a: "))
#         b = int(input("enter the value of b: "))
#         j = 1
#         win_no = random.randint(a,b)
#         while True:
#             c = int(input(f"Please press the number between {a} and {b}: "))
#             if c<win_no:
#                print("the number you entered is less")
#             elif c>win_no:
#                 print("The number is greater")
#             else:
#                 print(f"you win in {j} chances")
#                 break
#             j+=1
#             print(f"you have completed {j-1} chances")
#
#inp = input("do you want to play again so press c for another player and quit press q")
                 # if inp=='c':
                 #     continue
                 # elif inp=='q':
                 #     exit()
#
#



# a = int(input("enter the value of a: "))
# b = int(input("enter the value of b: "))
# win_no = random.randint(a, b)
#
# class game:
#
#     def __init__(self,name):
#         self.name = name
#
#     @classmethod
#     def input(cls):
#         return cls(input('name of the player: '))
#
#     def trial(self):
#         j=1
#         while True:
#             c = int(input(f"Please press the number between {a} and {b}: "))
#             if c < win_no:
#                    print("the number you entered is less")
#             elif c > win_no:
#                     print("The number is greater")
#             else:
#                 print(f"you win in {j} chances")
#                 break
#             j+=1
#         return j
#
# player1=game.input()
# player2=game.input()
# print(f" -{player1.name} Player 1 is playing...")
# l=player1.trial()
# print(f"{player2.name} - Player 2 is playing...")
# m=player2.trial()
# if l<m:
#    print(f"{player1.name} is the winner")
# elif l>m:
#     print(f"{player2.name}1 is winner")
# else:
#     print("...Match is draw...")
# users =[]
# for i in str(range(2)):
#      # user=game.input()
#      user=input('name of the player: ')
#      users.append(user)
#      users=game.trial()

    # if i[0] > i[1]:
    #     print(f"{i[0]} is the winner")
    # else:
    #     print(f"{i[1]} is the winner")


#     users[user.name] = user
# if user.name in users:
#     raise ValueError('Duplicate name')`
#
def guessgame(a,b,actual):
    guess=int(input(f"guess a number between {a}  and {b}"))
    nguess=1
    while guess != actual:
        if guess<actual:
            guess=int(input("Enter the bigger number: "))
            nguess+=1
        else :
            guess=int(input("enter the smaller: "))
            nguess+=1
    print(f"player complete in {nguess} chancs")
    return nguess


if __name__ == '__main__':
    a=int(input("Enter the value : "))
    b=int(input("Enter the value : "))
    actual1=random.randint(a,b)
    print("Player 1's turn")
    g1=guessgame(a,b,actual1)
    print("Player 2nd turn")
    actual2 = random.randint(a, b)
    g2=guessgame(a,b,actual2)

    if g1<g2:
        print("Player 1 won")
    elif g1>g2:
        print("player 2 won")
    else:print("its tie")

    print(f"The number for player 1 was {actual1} and for player 2 was {actual2}")