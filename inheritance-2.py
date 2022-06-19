# MULTIPLE INHERITANCE:- 2 CLASSES THI UNKA USE KRKE 3RI CLAS BNAYI GYI
class Employee:
    no_of_leaves = 8
    var=1       #then check here if here are the arguments then print them otherwise,
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The name of the Employee {self.name} with salary {self.salary} from {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        return ("this is good" + string)

#if a Programmer is a part time player as well
class Player:
    no_of_games = 4
    var = 2   #here and print this argument of the seecond classs
    def __init__(self,name,game):
        self.name= name
        self.game= game

    def printdetails(self):
        return f"The name is {self.name} and play {self.game} play{self.no_of_games}"

#if a programmer is player employee as well
# order is important
#Jb bhi hm kisi 2 class ko inherit krte hai to vo sbse phle constructor ko 1 pr rkhki hui class mai dhundega vha mila to aage bdhega then dusri class mai dekhega va pr jo bhi milega print krega
class CoolProgrammer(Employee ,Player):  #yha phle employee ko dekhega then player ko
     # pass
     var=3    #first print this class argument and then go to the first class which we define in the inherit way firstly employee then player
     # it is the only function which work on the particular class
     def language(self,language):
          self.language = language
          return f"language is {self.language}"

shubham = Employee("Shubham", 255, "developer")
manu = Employee.from_dash("Manu-555-CEO")

karan = Player("Karan", ["Cricket"])
tanu = CoolProgrammer("Tanu",678,"CoolProgrammer")     #here coolprogrammer clas is first searching the arguments in Employee class if they are completed then step up to player if there is nothing details we hav to print so it can move on to CoolProgrammer
# print(karan.printdetails())
print(tanu.printdetails())  #this is because we dont have any function perform in the coolprogrammer class so we have to specify it in printdetails
# print(tanu.language("c++"))   #ya to fstring mai constructor ke andr hi define krdo vrna to yha aakr aise alg se particular instance ko point krke print kra skte hai
# print(tanu.var)