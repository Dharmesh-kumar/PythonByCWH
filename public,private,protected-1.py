#public:- apke pss kuch info hai to ap use gate pr lga doge koe bhi use access ya deksh skta hai
#protected:- ap cahhte hai kio sirf apke ghrwale dekhe us paper ko to ap use ghr ke andr lga loge to use family members dekh skte hai
#private:- ap us paper ko apne pss chupakr rkhege apne room mai lga lege jis se sif ap hi dekh skein use

class Employee:
    no_of_leaves = 8     #this is public if we dont specify any access specifier onto it
    var=1
    _protect =2  #it is protector where it can use by base class as well as the derived class from the base class
    __private = 22 #it is the private variable which has __ underscore double and it cannot accesed anywhere
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


shubham = Employee("Shubham", 255, "developer")
print(shubham._protect)  #it print direcly the private bcause i can be accesed by the instance of the same base class
# print(shubham.__private)  #it cannot print like this because ye vha pr private hai but yha pr nhi krega kyki
# ye python ne krdiya "NAME ANGLING" to usko aise nhi access kr skte to uske liye apko
print(shubham._Employee__private)  #python ne ise aisa save kra kyki jis se ap glti se ise bahar acces na krlein direct bulakr to ye aise use ho
