#MULTILEVEL INHERITANCE:-
class Dad():
    basketball = 1
# dad ke pass apna sb kuch hga
class Son(Dad):
    dance= 1
    basketball = 2
    def isdance(self):
        return f"Yes i dance {self.dance} no of times"
# son ke pass apna saman bhi tha or usne dad ka bhi leliya
class Grandson(Son):
    dance = 6
    def isdance(self):    #if we remove this then we prin any isntance of tthis class so this is ooverride form the son so that method in son class isdance print as output
        return f"jackson yeah!"\
         f"Yes i dance very awesomly {self.dance} no of times"
#grandson ke pass apna hi saman tha or usnee son se bhi inherit krliya orr sath hi sath son ke pss dad ka bhi ssaman tha to vo bhi grandson inherit krlega
darry= Dad()
larry= Son()
harry= Grandson()
print(harry.isdance())    #print instance of harry which is Grandson and print its property in class if it is not here then the isdance print of the method in the Son class because it can herit form there
print(harry.basketball)   #here it print the basketball which is in the Son class if there is not  any basketball the it can take basketball from the dad classs because son inherit the properties of the dad

