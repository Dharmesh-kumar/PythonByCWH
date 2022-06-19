#program of number of guesses left and game over on n=18 and total guesses is  9
n=18
ng=1
print("number of guesses is limited to 9 times only: ")
while(ng<=9):
    guess_number=int(input("guess the numbr:\n"))
    if guess_number<n:
        print("the number you entered is less please enter the greater number")
    elif guess_number>n:
        print("the number you enter is greater please enter the larger number:")
    else:
        print("you won")
        print(ng,"is the number of guesses you took to finish it:")
        break
    print("the no. of guesses left: ",9-ng)
    ng=ng+1

    if(ng>9):
        print("game over")