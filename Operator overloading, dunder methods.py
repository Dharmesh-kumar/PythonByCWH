#SPECIAL FUNCTIONS __ se start hne wale methods or __ se khtm hne wale methods ko bolte hai DUNDER methods
#search mapping operators to functions:- for more dunder
class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):   #it is dunder INIT which is spcial method because it is constructor
        self.name = aname
        self.salary = asalary
        self.role = arole
        # return f"The name of the Employee {self.name} with salary {self.salary} from {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves
#operator oveloading :- it can overload object and tell them to do it specific tasks which dunder is define but its not compulary for all the objects
#if we have to ad the two objects then it can use dunder method behind the scene
    def __add__(self, other):  #this is add dunder
         return self.salary + other.salary
#ye sbhi parameters jo bhi hmne object ke liye pass kraye the instance varible bnakr to ye unhe lekr perform krega jo bhi hm special tasks isse krane cahhege vo like add dunder
    #for division
    def __truediv__(self, other):
         return self.salary / other.salary
# if we print simply object then there are shown the address of the instance but if we don't want to show that so we use tr and repr
    def __repr__(self):
        return f"Employee ({self.name}, {self.salary}, {self.role})"

    def __str__(self):
        return f"The name of the Employee {self.name} with salary {self.salary} from {self.role}"

emp1 = Employee("Man",555,"Programmer")
emp2 = Employee("Tanu",553,"Coder")
print(emp1+emp2)    #dunder add print
print(emp1.salary+emp2.salary)   #ya to aise krlo but agr hm dikhana nhi cahhte or direct andr se hi cll krana cahhte objects mai se to dunder method hai hi
print(emp1/emp2)    #dunder truediv print
print(emp1)   #see it is empty so that it can tke str automatically
print(repr(emp1))   #if str is already a dunder in function so that it canno print but if have to print repr so we have to specify it
