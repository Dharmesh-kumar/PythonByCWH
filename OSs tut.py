import os      #os is an inbuilt function which can tell the input of the mouse and keyboard basically it is managed the hardware this is operaing system but here this is moduleused for any inbuilt files and so on
# print(dir(os))
#Working directory:-
print(os.getcwd())   #get current working directory here the current wprking directory print
# os.chdir("E://")    #for changing directory
# print(os.getcwd())   #ab program ki current workin directory change klrdi to vo vha jakr dhundega
# #if i can open any the directory then
# f=open("docs.txt")     #so its doesn't found to be here because we change its drectory in the above code but if we remove that code so it can check its current working directory which as printeed ablove
# print(f.readline())
#
# #listing directory
# print(os.listdir())    #is particular directory ki saari list dedega hmein
#
# #for makin folder
# # os.mkdir("this")    #it cn make a folder in particular directory
# #if i want to make directories in the folder
# # os.makedirs("this/that")  #here this folder ke andr that folder bnjayga jise hm use bhi kr skte   USE:- subdirectories automatically
#
# #for rename
# # os.rename("change krdi manu","manu.txt")      #ye chnagr krdena kisi bhi file ka naam
#
# #environment varibles read
# # print(os.environ.get("Path"))
#
# #join:- join kredga kinhi 2 paths ko obtimal way mai jisme slashes ki tensn nhi hoti
# # print(os.path.join("c://","manu.txt"))
#
# print(os.path.exists("c://manu"))
# print(os.path.exists("c://Program Files"))#tells true or false
