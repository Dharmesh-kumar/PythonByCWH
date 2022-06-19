#fucntions
#bilt-in functions
a=9
b=8
c= sum((a,b))      #extra braces is used for the program not showing iterable and in thi we can use tuple for not change
print(c)

#user defined functions
def function1():     #defined function calling
    print("hello you are in function 1")
function1()        #here we can prnt the statement which is stored by user
function1()        #we can calling fucntion1 anytime anywhere in the program by just function() and use its statement
function1()
function1()

def function1(a,b):     #for giving the value in the output without stored it anywhere
    print("the number you entered is: ",a+b)
function1(5,7)

def function2(a,b):

    average=(a+b)/2
    print(average)
function2(5, 7)

 #for print the value of the functions in the variable
def function2(a,b):     #here variable calling values from the pre-defined function

    average=(a+b)/2
    return average
v=function2(5, 7)      #the return value stored in the v as a variable and then print v
print(v)

def function2(a, b):
    """this is a function which will calculate average of two numbers"""  # this is a doctsrting:-function ke andr pehli likhi hui comment doct string hoti hai
    average = (a + b) / 2
    return average
print(function2.__doc__) # when there are more than 100 functions in a program so its print doctsting


