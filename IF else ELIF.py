#if else condition
var1 = 4
var2 =6
print("enter the value you entered for checking:")
var3 = int(input())
if var3>var2:            #if condition check
    print("greater")
if var3==var2:              #checking next statement after checking previous one
    print("equal")
else:                    #else condition checking
     print("lesser")

  #if we have to check the statement directly to the correct statement we use elseif or in python elif
var1 = 4
var2 =6
print("enter the value you entered for checking:")
var3 = int(input())
if var3>var2:
    print("greater")
elif var3==var2:
    print("equal")
else:
     print("lesser")

list1=[5,6,3]           #check the element is in the list or not and display the list
print("enter the value for checking it is in the list: ")
a=int(input())
if a in list1:        #the element is checking its in the list
    print( a in list1 )   #true button checking
    print("it is in the list at: ",list1.index(a))   #print the postion of the element in the list
elif a not in list1:
    print(a not in list1 )   #false button checking
    print("it is not in the list")
print("here is your list",list1)

print("enter you age: ")
age=int(input())
if age<18:
    print("you cannot drive")
elif age==18:
    print("we will think about you")
else:
    print("you can drive")






