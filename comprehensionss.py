a,b,d= map(int,input("Enter the input: ").split(" "))   #onle lin e inpput any variables
e=a+b+d
print(e)
#manlo apko ek list banani hai numbr divisble by 3
#list comprehension
# ls=[]
# for i in range(100):
#     if i%3==0:
#         ls.append(i)
# print(ls)
#OR
ls=[i for i in range(100) if i%3==0]
print(ls)

#dictionary comprehension
# dict1={0:"item0",1:"item1"}   #and so on
#OR
# dict1={i:f"item{i}" for i in range(100) if i%10==0}
dict1={i:f"item{i}" for i in range(5)}   #for opposite key value pairs
dict2={value:key for key,value in dict1.items()}
print(dict1,"\n",dict2)

#set comprehension
dresses={dress for dress in ["dress1","dress2",
                             "dress1","dress2",]}
print(type(dresses))   #it can give set  because not having value
print(dresses)

#generator comprehension
even=(i for i in range(100) if i%2==0)
print(type(even))    #paranthesis print generator
# but if we print so it can give address so if we have to take values we have to print __next
print(even.__next__())
print(even.__next__())
print(even.__next__())
# for i in even:   #OR
#     print(i)

for i in range(0, (int(input("enter the number: "))+1)):print(i,end=", ")

