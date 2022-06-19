#how to write a file
f=open("Dharmesh3.txt", "w")     #write mode as text which clear the previous text from the file and add new
content=f.write("Dharmesh bht aacha hai")
print(content)
f.close()     #here this format is used to delete the previous text and print the

#append in the file or addtext in the file
f=open("Dharmesh2.txt","a")   #for append add the text into the file along  with previous
f.write("Dharmesh bht aacha hai\n")
a=f.write("Dharmesh bht aacha hai\n") #numbr of characters print in the file
f.close()

#handle read and write both in the file
f=open("Dharmesh.txt","r+")   #r+ is udes for both read and write
print(f.read())
f.write("thank you")
