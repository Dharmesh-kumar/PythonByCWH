#operators and its type
"""
arithmetic operators :for numeric calculation (+,-,*,/,//,**,%)
assignment operators: for assign the value and constant will become variable (=)
comparison operators: for compare the variables with their condition (==)
logical operators: and , or ,not
identity operators: is & is not
membership operators: in & not in
bitwise operator: bonary numbers 0,1
"""
#arithmetic operator
print("5+6 is", 5+6)
print("5-6 is", 5-6)
print("5*6 is", 5*6)
print("5**6 is", 5**6)  #for finding exponential operator
print("5/6 is", 5/6)
print("5%5 is", 5%5)     #for print the remainder modulus operator
print("15//6 is", 15//6)  #floor division operator on double divide the value it will give the exact integer

#assignment operator
print("assignment operators")
x=5
print(x)
x +=7    #adding the number in the variable +,-,/,%
print(x)

#comparison operator
print("comparison operator")
i=8
print(i==5)
print(i !=5)

#logical operators
a= True
b=False
print(a and b)      #and operator is g iving output when both are true or false it will give output on both the conditions
print(a or b) #or operator is workking on the true condition if in both one is true it will print ture a or b
print(a is not b)
#identity operators
a=True
b=False
print(a is b)
print(a is not b)
print(5 is not 5)

#membership operators4
list=[3,3,2,2,38,55,45]
print(324 not in list)

#bitwise operators
"""
0 - 00
1 - 10
2- 01
3- 11
"""

print(0 & 1)   #print 0 because 0 and 0 is  A.B
print(0 | 1)   #print 1 because 0 or 1 is 1 A+B
print(0 | 3)
"""for 0-00
       3-11
    or   11 -3     
"""
