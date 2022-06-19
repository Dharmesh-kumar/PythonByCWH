#lambda functions or anonymous fucntions
def add(a,b):
    return a+b

def sub(x,y):
    return x-y

minus = lambda x, y: x-y    #it is one liner function replace for function process
plus = lambda  x, y:x+y


print(minus(9,4))    #here the value print from the function minus
print(plus(9,4))     #here the value print from the plus lambda function
print(add(2,3))      #the value call from the function add
print(minus(2,4))    #the value call from the lambda fucntion

def a_first(a):
    return a[1]     #1 index in the list return by it

a=[[1,14], [5,6],[8,23]]
a.sort(key=a_first)         #key is an argument which function as a input into it
print(a)

# or we can do ir direct
a=[[1,14], [5,6],[8,23]]
a.sort(key=lambda x:x[0])         #key is an argument which function as a input into it
print(a)