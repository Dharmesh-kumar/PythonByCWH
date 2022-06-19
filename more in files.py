#more important functions in python
f=open("Dharmesh.txt")
print(f.readline())
print(f.readline())
#if we have to read big files and know where the file pointer is in the file
f=open("Dharmesh.txt")
print(f.tell())
print(f.readline())
print(f.tell())           #tell function tells point at which the pointer is
print(f.readline())
f.seek(6)                   #reset the line at which you want to seek
print(f.readline())
f.close()