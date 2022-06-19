import re
mystr='''
hello my name is Dharmesh chauhan and i want to give a try in the software field like i want to do
the machine learning algorithm and want to make a PORTAL COMPANY which is based on the removal of the vastly keyboard use like 
there are many workers behind this project so you have to work on that 
different fields please for more Enquery contact 19bcs2498@gmail.com and you have our developer Thakurdharmesh555@gmail.com 
and my partner priyanshuchauhan7840@gmail.com
# '''
l1= re.findall(r"\w+@\S+\w",mystr)   #best way to do like from the white space character
#r"[0-9a-zA-Z._+%]+@[0-9a-zA-Z._+%]+[.][a-zA-Z.0-9]+"   these are the occurancs we need so make a procedure of it
with open("email_store.txt","a") as f:
     j = 1
     for i in l1:
         f.write(f"Email{j}:{i}\n")
         j+=1
     f.close()

print(f"Email's are: {l1}")
print(f"Total Email's are: {j-1}")


#or
# email=re.findall(r"[0-9a-zA-Z._+%]+@[0-9a-zA-Z._+%]+[.][a-zA-Z.0-9]+",mystr)
# print(email)