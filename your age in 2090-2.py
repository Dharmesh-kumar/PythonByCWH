# take input as a age or year of birth from the user and tell them they turn 100 years old,they can then optionally provide ayeaer and your program must tell thier age in that perticular year
# you should be handled all errors:
#   you are not born yet
#   you seems to be alive oldest
#    and others error if possible

current_year = int(input("Enter the current year: "))
while True:
    age = int(input("Enter you age or your birth year: "))
    if len(str(age))==4 and age>1880:
        if age>current_year:
            print("You are not born yet")
            print("Try again")
            continue
        elif age<1920:
            print("You are the oldest person living")
        elif age<current_year+1:
            temp= age+100
            print(f"you will turn 100 at {temp}")

        tell_age=int(input("Enter a year so that we will tell you your age in that year:"))
        if tell_age<age:
            print("sorry you are not born yet")

        elif tell_age>=age:
            temp=tell_age - age
            print(f"your age at the {tell_age} is {temp}")
        else:
            print("Wrong input")

    elif age>0 and len(str(age))<4:
        if age==100:
            print("You already 100")
        elif age>120:
            print("You are enough old here")
        elif age>100:
            print("You already cross 100")
        elif age<100:
            temp = 100-age
            temp= current_year+temp
            print(f"You will turn 100 in {temp}")
        tell_age = int(input("Enter a year so that we will tell you your age in that year:"))
        temp=current_year-age
        if tell_age<temp:
            print("you are not born yet")
        elif tell_age>=temp:
            temp=tell_age-temp
            print(f"You will be {temp} yeas old in {tell_age}")
        else:
            print("Wrong input")
    else:
        print("The input is not valid")
        continue

    _input=input("If you want to quit the program enter 'q' and for continue press 'c': ")
    if _input=='q':
        exit()
    elif _input=='c':
        continue