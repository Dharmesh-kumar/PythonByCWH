# CLASS METHOD DECORATOR
class Employee:
    no_of_leaves=8
#if i w ant to chaangee the number of leaves from the function so that assign them in this function and can be acccesed by instances
    def __init__(self, aname, asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name} Salary is {self.salary}  and role is {self.role} having {self.no_of_leaves} leaves"
#if we want to improve latency in the program so for avoid self we use CLASS METHOD DECORATOR
    # cls hai vo class jiska instance hai object jispr function run kr rha hai
    @classmethod   #class method hmara only us class ske kisi bhi instance variable ko access kr payga or hm ise kisi class ya fir instance dono se bhi access kr skte hai
    def change_leaves(cls,anewleaves):        #why here is  cls(class) not self because maine ye class method bnaya hi isiliye the ki mjhe sirf class mile or mai uski sath khilvad kr sku
        cls.no_of_leaves = anewleaves
        # or ise use krne ke baad hm agr kuch bhi chnge krein to vo puri class ke attribute ko chnge krdega
# USE:- We can use clasmethod as an  ALTERNATIVE CONSTRUCTOR
manu = Employee("Manu", 455, "Instructor")
rohan =Employee("Rohan",4554,"Student")
rohan.change_leaves(34)  #see yha pr mne rohan ki no.of.leaves chnge kri but class attribute k vjhse ye
print(manu.no_of_leaves)  #manu ki bhi chnge krdi isne
# Employee.change_leaves(34)  #class method ka object hai jo self ke jgh cls se chlega particular object ke liye

# Employee.no_of_leaves =89   #for avoid this use function instead of using particular instance or use class so we used as class method
print(manu.printdetails())
print(rohan.printdetails())
