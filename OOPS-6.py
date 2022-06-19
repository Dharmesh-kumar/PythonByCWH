#STATIC METHOD(SAADA METHOD):nahi object method access krne or nahi class  method to fir mjhe ek aisa method chiye jise hme usko class ke andr krhna ho to hm inhe ise use krte hai
class Employee:
    no_of_leaves=8

    def __init__(self, aname, asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name} Salary is {self.salary}  and role is {self.role} having {self.no_of_leaves}"
#Chizzo ko precise krne ke liye or jitni resources hme chiye isiliye hm classs method use krte hai or static methid
    @classmethod
    def change_leaves(cls,anewleaves):
        cls.no_of_leaves = anewleaves

    @classmethod
    def from_dash(cls,string):   #pass string as an argument
        return cls(*string.split("-"))   #and then argument as *args use and then split by"-" dash
#aisa funcntion bnana ho jo nahi self ko as an argument le or nahi class ko bs kre kya ki sirf khud apne ap me hi kaam kre
    @staticmethod   #hmne isme classs mai isiliye dala jis se ye Employee ke andr objects ke liye hi kaam kre bs
    def printgood(string):
        print("This is good " + string)

        # return "thinga"     #return value btaygi ki kya iski value hgi agr mai printgood ko bhi print krau tb return use hga vrnaa none print krega kyki isme kuch hai hi nhi
manu = Employee("Manu", 455, "Instructor")
rohan =Employee("Rohan",4554,"Student")
karan =Employee.from_dash("Karan-480-student")
Employee.printgood("Manu")

print(karan.printdetails())
print(manu.printdetails())
print(rohan.printdetails())

