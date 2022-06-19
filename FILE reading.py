# how to read the content from a particular file
f=open("Dharmesh.txt")     #here f is the file pointer which open file of the name
content = f.read() #now which task you want to done in the file with the pointer
print(len(content))
print(content)

f.close()                   #close the file as it is

#if we want to print the content of the file in various forms then
f=open("Dharmesh.txt", "rb")     #rb is used for the read as a binary
content=f.read()
print(content)
f.close()

f=open("Dharmesh.txt", "rt")     #rt is used for the default text read
content=f.read(3)  #here we also print the indexes of the word
print(content)
f.close()

f=open("Dharmesh.txt", "rt")
content=f.read(23)  #in which all the words in the txt file print as per index
print("1:",content)      #but if we can slice it then

content=f.read(38)
print("2:",content)

content=f.read(22)
print("3:",content)
f.close()
#edit particular iteration in the file for reading line by line
f=open("Dharmesh.txt", "rt")
for line in f:          #new line charactere print by default because its already in the file
    print(line)

#readline function
f=open("Dharmesh.txt", "rt")
print("\n",f.readline())
f.close

#if you want to store all lines in list
f=open("Dharmesh.txt", "rt")
print(f.readlines())
f.close()