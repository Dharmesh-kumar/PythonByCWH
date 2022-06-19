#simple imheritance:-inherit the property of the class into another class
class Employee:
      no_of_leaves = 8

      def __init__(self, aname , asalary ,arole):
          self.name = aname
          self.salary = asalary
          self.role = arole
          # self.language = alanguage

      def printdetails(self):
          return f"The name of the Employee {self.name} with salary {self.salary} from {self.role}"
      #here define thee new leaves for the particular instance of which we have to change without passing it into constructor use class method
      @classmethod
      def change_leaves(cls,newleaves):
          cls.no_of_leaves=newleaves

      @classmethod
      def from_dash(cls, string):
          return cls(*string.split("-"))

      @staticmethod
      def printgood(string):
          return("this is good"+ string)
#code reuseability introduces the inheritance with having th property of the another class and having with the property of same class
#here inherit the property of the Employee class into the programmer
class Programmer(Employee):  #here we form a new class programme which can take all the methodss and the attributes from the Employee and use their own for define them
    #if we want to create its own details so we have to specify them in its own constructor
    #Overriding:- if i want to override the another variables for the particular class and dont want to print the other class variables without deleting it so we can override them here as well for the convinience
    no_of_leaves = 22      #here the number of leaves is diffrent from the Employee class leaves
    def __init__(self,aname , asalary ,arole,alanguages):
        #here we have two options we can specify or copy Employee class define arguments here or we can use SUPER
# Error:    #Alternative = super :- it can run super class functions instructions into the sub class whic comes in overriding
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages = alanguages
    def printprog(self):
        return f"The name of the Employee {self.name} with salary {self.salary} from {self.role} working in {self.languages} having {self.no_of_leaves}"

karan= Programmer("Karan",666,"Programmer","C++")
harry= Programmer("Harry",444,"Programmer","Python")
shubham = Employee("Shubham",255,"developer")
manu = Employee("Manu", 555,"CEO")
tanu = Employee.from_dash("Tanu-666-Manager")
# Employee.no_of_leaves(10)
#these are the instances which comes in the Employee class  and print their function with only their properties
print(manu.printdetails())
print(shubham.printdetails())
print(tanu.printdetails())
# here these are the details which is in the only programmer class and it can print the employee class with the programmer having their propert as well
print(karan.printprog())
print(harry.printprog())