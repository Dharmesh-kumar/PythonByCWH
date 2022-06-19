# OBJECT INTROSPECTION?:- kisi bho object ke baare mai jaankaari lena uske baaare mai k kha se aaya hai kis type hai pouri jaankari lena hi introspection hota hai
class Employee:
    def __init__(self,fname, lname):
        self.fname = fname
        self.lname = lname

    def Explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return "Email not set please set it using setter"
        return f"{self.fname}.{self.lname}@portal.com is your email"

    @email.setter
    def email(self, string):
        print("Setting now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        print("Deleting now...")
        self.fname = None
        self.lname = None

skillf = Employee("skill","F")
# print(skillf.email)
print(type(skillf))
print(type("This is a string"))   #ye this is string str se aara hai
print(id("this is a string"))   #kisi  bhi particular fuynction ki id backend mai save hoti hai to vo aise print kr skte hai
print(id("this is a that"))
print(dir(skillf))    #jo saare functions or directories jo hai skillf ki jis se vo run hora hai vo print kr dega

#INSPECT MODULE
import inspect

print(inspect.getmembers(skillf))    #saaare ke saarre members aajayge or attributes inspect krne see or aise hi kaii saare hm introspction kr skte hai is module se direct isko import krke