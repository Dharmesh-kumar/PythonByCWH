# write a program which will keep adding a stream of numbers inputted by the user. The adding stops as soon as usewr presses q on the keyboard

sum=0
while True:
    user_input= (input("Enter the price or press 'q' to quit: "))
    if (user_input!='q'):
        sum=sum + int(user_input)
        print(f"you bill total is {sum}")
    else:
        print(f"you bill total is {sum} . thanks for shopping with us")
        break