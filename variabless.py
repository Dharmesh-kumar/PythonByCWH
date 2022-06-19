#variables
var1 = "Dharmesh"
var2 = 4
var3 = 24.5
var4 = "chauhan"
print(var1)

#types of variables
print(type(var1))
print(type(var2))
print(type(var3))

#concatination
print(var1 +  var4)

#typecasting between variables
var1 = "34"  #it is string if we add inverted comma's
var2 :str = "23"
print(var1 + var2)
  #so we have to add string in number as a integer
print(int(var1) + int(var2)) #here we specify the variable as a string so we have to put int after the result

#to print string many times
var1 = "Dharmesh\n"
print(10 * var1)

#cant use normally as in integer
var1 = "34"
var2 = "23"
print(10 * int(var1) + int(var2))
    #so we have to make integer portion as astring and then print 10 times
print(10 * str(int(var1) + int(var2)))

#input from user
print("enter your number: ")
inpnum = input()  #as a string goes to inpnum variable
print("the number you entered", inpnum)
print("the number you entered", (inpnum) * 10)
print("the number you entered", int(inpnum) * 10)

#adding two numbers from user
print("enter your first number:")
n1=input()
print("enter your second number:")
n2=input()
print("the addition of the numbers:   ",(int(n1) + int(n2)))

