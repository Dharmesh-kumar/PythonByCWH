#try except handling
num1= int(input("enter num1:"))
num2 =int(input("enter num2:"))
try:                 #try out the code and print the value of the sum
    print("the sum of the tow numbers is: ",int(num1+num2))    #here the code is complete
except Exception as e:  #if you wannt to enter the another information in such case you internet or code doesnt work then print another ecxeption
    print(e)
print("this line is very important")
