'''its result day at school and everone is not happy you decided to make your friend laugh by jumbling their names to comeup with some funny names.
your program should take the number of names ad the names seperated by space as input. output should be funny names as the same order

input:
Enter number of friends:
3
Enter the bname of yoppur 3 friends:
manu chauhan
tanu chamar
ishu  bhngi

output:
manu bhngi
tnau chauhan
ishu chamar'''

import random

def jumble_words(fname,lname,number):
    for i in range(0,number):
        jumble_name = fname[i]+" "+lname[random.randint(0, number-1)]
        print(jumble_name)

if __name__ == '__main__':
    number = int(input("Enter the number of the players: "))
    namelist = []
    fname = []
    lname = []

    for i in range(1,number+1):
        name= input("Enter the name: ")
        namelist.append(name)

    for i in namelist:
        split_name= i.split(" ")
        fname.append(split_name[0])
        lname.append(split_name[1])
    jumble_words(fname,lname,number)