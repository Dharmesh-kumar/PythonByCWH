#slicing of lists in string
grocery = ["harpic", "vim bar", "deodrant", "bhindi", "lollypop", 56, 55]
print(grocery)
print(grocery[2])
print(grocery[0:7:2])
print(type(grocery))
for items in grocery:
 if str(items).isnumeric():  #only print the numbers in the list
      print(items)
numbers = [2, 7, 9, 11, 3]
print(numbers)
numbers.index(3)
print(numbers)

print(numbers[2])
   #sorting of the numbers in above lists
numbers.sort()
print(numbers)
 #reverse of the sorting list
numbers.reverse()
print(numbers)
print(max(numbers))  #to find out maximum number
numbers.append(4)  #to add another number in the end of the list
print(numbers)


numbers.insert(1,22)  #at 1 index print 22 in the list of the numbers
print(numbers)
numbers.remove(9)  #to remove the numbere from the list
print(numbers)

numbers = [2, 7, 9, 11, 3]
numbers.pop()        #to remove last element from the list
print(numbers)
print(numbers)
    #to change values
numbers[1]= 98   #at 1 index change to 98
print(numbers)

             #mutable - can change  (list)
             #immutable - cannot change
 #tuple (immutable)
tuple = (2,3)      #tuple is used in the parantheesis
print(tuple)

#for input the list
list2=[]
for items in range(0,5):
    a = input("enter the more food: ")
    list2.append(a)
print(list2)
#swapping
a=1
b=2
a,b=b,a
print(a,b)

# list=[]
# n=(input(print("the first food: ")))
# while True:
#     if int(n)<5:
#            list.append(input(n))
#     print(list)
#     n=n+1
#     break
# else:
#       print("limit complete")



