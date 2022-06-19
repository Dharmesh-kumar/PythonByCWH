n=int(input(print("Enter the number of rows: ")))
boolint=int(input(print("Enter 1 or 0 as input: ")))

if bool(boolint)==1:
    print("Star Pattern : \n")
    for i in range(0,n+1):
            print("*"*(i))
elif bool(boolint)==0:
    print("Inverted Star pattern : \n")
    while (n != 0):
        print("*" *(n))
        n = n - 1
else:
    print("enter only 1 or 0 ")