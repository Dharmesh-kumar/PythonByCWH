  #dictionary in python

d1={}     #for sets dictionary use this braces
print(type(d1))

d1=[]      #for list dictionary use this brackets
print(type(d1))

d1=()       #for tuple dictionary usee this paranthesis
print(type(d1))

d1= {"AI":"Portal" , "Construction & builder": "M & T", "Aero":"Omega"}   #here the element has  its own objects and show it as the dictionary
print(d1)

d1={"Manu":{"AI":"Portal", "Nano":"GPS","cloud":"processor"},"tanu": "M & T", "Mohit":"chicken"}    #ypu can add subdictionary in the dictionary
print(d1["Manu"])           #for print subdictionary
print(d1["Manu"]["Nano"])    #for print subdictionary particular element
print(d1.get("tanu"))       #for print the particular element
d1["Aero"]= "Omega"   #to add another element in the dictionary without changes into it
print(d1)
d2=d1     #if you add another dictionary and connect them if we want to remove an element from d2 then it automatically reemove from d1 alsso
d2=d1.copy()     #if we don't want to remove the element then we shouuld do it like it
del d1["Mohit"]              #for delete the particular element from dictionary
print(d1)
d1.update({"papa":"property"})
print(d1)
print(d1.keys())    #to print all the keys in the dictionary
print(d1.items())    #print key value pairs

#Dictionary input from user
d1={"Manu":{"AI":"Portal", "Nano":"GPS","cloud":"processor"},"tanu": "M & T", "Mohit":"chicken"}
print("enter the word you want to choose: ")
word=input()
print("the work by all which you entered is owned by: ",d1.get(word))
print("the work by Manu which you entered is owned by company:",d1["Manu"].get(word))
