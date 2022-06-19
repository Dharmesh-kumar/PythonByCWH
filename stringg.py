#string datatype print
mystr = "Dharmesh is a good boy"
print(mystr)

#suppose we have to take any alphabet from the above string
print(mystr[4])

#if we have to take out word (string slicing)
print(mystr[0:8])   #o including and 8 excluding in the program

#length of the string
print(len(mystr))  #these are 22 but index starts from [0:22] because 22 is excluding
print(mystr[0:22])
print(mystr[0:98]) #we can write as also its gave only the 0 to any of we enter in string if okk to ne not 98

#to skip the character from the string (advanced slicing)
print(mystr[0:8:2])
print(mystr[:]) #initial index is automatically 0 and final length of index is  total string length
print(mystr[3:13:3])  #space of 3 write is due to excluding but is really 2
print(mystr[::])  #[0:22:1] according to the above mention string

   #negative index
print(mystr[-22:-14])  #negative index starts from opposite side from -1 to left side of the sting
print(mystr[-1:-23:-1]) #to reverse order of the string

#boolean datatype(true or false)
print(mystr.isalnum())  #isalphanumeric is a datatype which means that the string iss spaceless
mystr = "1Dharmeshisagoodboy"
print(mystr.isalnum())#both alphabetical and numererical so isalnum
print(mystr.isalpha()) #it is alphabetical term
print(mystr.isnumeric()) #the whole mystr is numeric so its not which is false
print(mystr.endswith("boy"))  #string end with boy which is true
print(mystr.endswith("bdoy"))  #string doesnt ends with bdoy which is false
print(mystr.count("h"))  #function which count the alphabet 'h' in the string

mystr = "dharmesh is a good boy"
print(mystr.capitalize())  #which capialize the first letterr of the string automatically
print(mystr.find("is"))  #the string at which position of index 'is' is present
print(mystr.lower())  #tp print string in lower case
print(mystr.upper())  #to print string in the capital letters
print(mystr.replace("is","are"))    #replace any word from anywhere in string
print(mystr.removeprefix("dharmesh"))    #remove first word from the string
print(mystr.__add__(" \nand Portal CEO"))  #add any string set in the string
mystr = "Dharmesh is a good boy and PORTAL CEO"
print(mystr.removesuffix("CEO"))#remove end word from the string
#this is used for print in vertical like list
for item in mystr:
    print(item)