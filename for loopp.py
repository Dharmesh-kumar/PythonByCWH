#for loop
list1=["manu","tanu","papa","mummy","pita Ji"]     #for print the list in for loop in rows
for item in list1:
      print(item)
#list of list in for loop
list1=[["manu",1],["tanu",2],["papa",3],["mummy",4],["pita Ji",5]]     #for print the list in for loop in rows
print(list1)
for item in list1:       #print item which is in the list
      print(item)
#unpacked the list
for item, lollypop in list1:    #for every iteration print the lolly with all the list
    print(item,"and lolly is",lollypop)
#for adding the list into the dictionary or list to dictionary typecasting
dict1=dict(list1)
print(dict1)
for item, lollypop in dict1.items():             #for every iteration in dictionary
    print(item,"and lolly is",lollypop)

#program to print the list number greater than and equals to 6 and then print the nu,bers only
list=["Dharmesh",5,6,7,8,77,99,44]
for item in list:
    if str(item).isnumeric() and item>=6:
        print(item)
