#a class which behave as a base class
#if we have the instructions for all the fclasses for which they have to do so we can use abc matter class un adeshoo ko jaari krne ke liye
# from abc import ABCMeta, abstractmethod  #here abstract method is a decorator in pythom abc module in built in python already
#we can use also this
from abc import ABC , abstractmethod
class Shape(ABC):    #if we use ABCMeta from class abc then we have to specify (metaclass=ABCMeta)  in class because it casn
    @abstractmethod   #ye jo hai sbko print krnas hai or ye anstract method hai iska mtlb ye define hai(mtlb hmne iska ye printarea krne ka hissa sbko boldiya ki krna hai like abstract krdiya sbme)
    def Printarea(self):
       return 0
# shape wali class aadesh de rhi hai ki printarea naam ke function ko implement krna hai
class Rectangle(Shape):      #inherit shape class for the print area of all the functions
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.length = 6
        self. breadth = 7
    def Printarea(self):                 #isne apna area print kra jaisa ki abstractmethod ne bola krne ko agr ye nhi krega to ye error bthrow krega
        return self.length * self.breadth

rect1 = Rectangle()
print(rect1.Printarea())
#hm directly object nyhi bna skte abstract class ka like
# tryobj=Shape()