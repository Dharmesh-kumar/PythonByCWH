# alternate of the for loops in the short term
#---------------------------MAP--------------------------------------
# map function:-kisi bhi ek fucntion ko puri list mai access kr deta hai
numbers =["3","34","64"]
# for converting elements in list from int to str
for i in range(len(numbers)):
    numbers[i]=int(numbers[i])
numbers[2]=numbers[2]+1
print(numbers[2])

numbers =["3","34","64"]
# print(map(int,numbers))      #map object at the memory location
numbers= list(map(int,numbers))   #list mai typecast kiya or map function ne numbers namak list ke saare elementss mai int functions ko chla diya
numbers[2]= numbers[2] + 1
print(numbers)

def sq(a):
    return a*a

num= [2,3,4,67,7,8]
square= list(map(sq,num)) #list mai typecast kiya or map function ne numbers namak list ke saare elementss mai square functions ko chla diya
print(square)

#we can use lambda in place of function
num= [2,3,4,67,7,8]
square= list(map(lambda x: x*x,num))      #ek aisa function jisko x pkdaya jaaye vo x*x krega laambda mai
print(square)

def square(a):
    return a*a

def cube(a):
    return a*a*a

func=[square, cube]
for i in range(5):     #i jo hn valaue chlaega 0 to 5
    val= list(map(lambda x: x(i),func))     #x ek aisa function jisko ap ek function ka naam pkdaao to vo i ko return krega with function
    print(val)
#------------------------filter-----------------------------------
#filter fucntion:ye ek aisi elements ki list bnata hai jispe given elements true print ho
list_1=[1,2,3,4,5,6,7,8,9]
def is_greater_5(num):
    return num>5          #it is the function where the element is true otherwise false

gr_than_5=list(filter(is_greater_5,list_1))   #if we use map here than it can map where the number is greater than 5 like it true or false so we can use filter for the exact print the numbers
print(gr_than_5)

#-----------------------reduce------------------------------------
#reduce:- its a part of functool module

list1=[1,2,3,4]
#if we want to print the numbers with for loop
num=0
for i in list1:
    num=num+i
print(num)
#for one line use functools python module nd reduce function for improvement of performance
from functools import reduce

list1=[1,2,3,4]
num=reduce(lambda x,y:x+y,list1)
print(num)
