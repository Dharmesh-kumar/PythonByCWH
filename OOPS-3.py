# CONSTRUCTOR:- class ko hi arguments dene ke trike ko hi constructor kehte hai
class Employee:
    no_of_leaves=8

# ye constructor hai in which we can accept argument of instance
    def __init__(self,aname,asalary,arole):     #ye jo aname hai vo arguments hai jo asssign krege instance ko iske andr
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):                #self:-vo object jiski baat ki jaa rhi hai automatic it print only inside the class when we defined details in function
#jb bhi manlo mai kisi instance ko acces kruga is se to self hojayga vo instance ka naam
           return f"The Name is {self.name} Salary is {self.salary}  and role is {self.role} having {self.no_of_leaves}"
manu = Employee("Manu",455,"Instructor")     #agr mai apne class ke naam ko koe argument dedu to vo constructor(init) mai pass hojayge
rohan =Employee("Rohan",4554,"Student")

# if we dont want to create these objects manually so we used constructor which can be created in the assign of object to class
# manu.name="Manu"
# manu.salary= 455
# manu.role="Instructor"
#
# rohan.name="Rohan"
# rohan.salary=4554
# rohan.role= "Student"

#constructor se bhi hm inhe direct acces kra skte hai bina kuch details aage bdhaye ek sath class ke andr arguments define krke
print(rohan.printdetails())  #printdetail ke andr rohan apne ap acess krjayga yha se direct self acces kr lega vo
print(manu.printdetails())