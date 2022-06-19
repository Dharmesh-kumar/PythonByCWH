#design a calculator which will correctly solve all thhe problems except
#the following ones faulty calculator
a=int(input("enter the value of first number: "))
b=int(input("enter the value of second number: "))
print("what do you want to choose between operators: +,-,*,/")
op= input("enter the operator: ")
if op=="+" and a== 59 and b== 9:
    print(77)
elif op=="+":
      print(a+b)
elif op=="-":
    print(a-b)
elif op=="*" and a==45 and b==3:
    print(555)
elif op=="*":
    print(a*b)
elif op=="/" and a==56 and b==6:
     print(4)
elif op=="/":
     print(a/b)
else:
    print("error")