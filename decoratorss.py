def function1():
    print("Subscribe now")

func2=function1
del function1    #if I delete func1 then its already save in the function2 as well variable
func2()            #so pehla function delete ho chuka ab ye print krega func2 ke built-in function ko

#function in function
def funcret(num):
    if num==0:
        return print
    if num==1:                #here both sum and print are functions
        return sum
a=funcret(1)
print(a)         #a function can return a function also

#we can also return function as an argument
def executor(func):      #here func is an argument in the function
    func("This")

executor(print)

# ------------------------------------DECORATORS----------------------
#isme dec1 naam kaa function bnayaa isko mai kuch bhi function dunga us se phle or uske baad mai executed or vo sb print statements print hgi
def dec1(func1):       #ye wala function koe return nhi krega ye use krega dusre function ko as an argument
    def nowexec():
        print("Executing now")     #kaaam krne se phlee
        func1()    #this is calling the values from the func1 argument
        print("Executed")       #kaam krne ke baad ye print hga agr mai kuch kaam kr rha hu to
    return nowexec
#so here is process for passing the func with another func and follows as argument into it
def who_is_Dharmesh():
    print("Dharmesh is a good boy")
who_is_Dharmesh=dec1(who_is_Dharmesh)    #ab who is dharmesh nhi rha function vo ab dec1 se calling hgyi or ab vo usme se process krke nowexec function return krega
who_is_Dharmesh()

#but if we dont want to pass the function to another function so we have to use as command
@dec1
def who_is_dharmesh():
    print("He is a good boy")
who_is_dharmesh()

#EK HI KAAM 10 FUNCTIONS KE KAM KRNA HO TO BLUEPRINT BNAKR UNKO DEC1 KRKE USE KRO
