#CLASS METHOD DECORATOR AS AN ALTERNATIVE CONSTRUCTOR
class Employee:
    no_of_leaves=8

    def __init__(self, aname, asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name} Salary is {self.salary}  and role is {self.role} having {self.no_of_leaves}"
  #CLASSMETHOD:-this is for change all the objects numbr of leaves as new which you can assign in function
    @classmethod
    def change_leaves(cls,anewleaves):
        cls.no_of_leaves = anewleaves
  #CLASSMETHOD:-this is for agr hmare pass bht saare entries hai to hmne string mai enter krayi or firi parse krdi alg alg split krke args ke through(kyki list thi) fir uske baad print kradi seperarte krke
    @classmethod
    def from_dash(cls,string):         #cls ko input le or string ko le or usise pura object bnade
        # params = string.split("-")    #params is a list where items are split as the string into diffrent items
        # print(params)  #it shows here is the list
        # return cls(params[0],params[1],params[2])  #ek aisa constructor jo arguments na lekr ke apne ap objects return krta hai
    #if use one liner by args
        return cls(*string.split("-"))   #list mai *lgate hi ye apne ap hi as an argument pass hojayge
#teeno parameters alg aalg pass krane pde as an argument to is se bchne ke liey
manu = Employee("Manu", 455, "Instructor")
rohan =Employee("Rohan",4554,"Student")
# aise string mai alg alg pass kranae ke liye init mai to hm ise aise use krege
karan =Employee.from_dash("Karan-480-student")  #phle class define kri fir ek srring define krdi proper

print(karan.printdetails())
print(manu.printdetails())
print(rohan.printdetails())

