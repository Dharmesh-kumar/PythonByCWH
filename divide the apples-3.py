# harry potter has n number of apples . harry has some students whom, he wants to distribute the apples, these n number if apples are providedd to harry by his friend ,
# and he can requests for few more or few less apples
#     you need to print weather a number in range mn to mx is a divisor of n or not
# input: take input n ,mx,mn from the user
# output: print weather the numbers between mn and mx are divisor or not

n=int(input("Enter the values of the apples: :"))
mn=int(input("Enter the minimum values of the apple : "))
mx=int(input("Enter the maximum values of the apple : "))

for i in range(mn,mx+1):
    if n%i==0:
        print(f"{i} is the divisor of {n}")
    else:
        print(f"{i} is not divisor of {n}")
