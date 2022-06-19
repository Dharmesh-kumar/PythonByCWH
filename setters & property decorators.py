#PROPERTY DECORATORS
"""phle maine constructor ke email naam ke attribute ko chlaya or fir jb hme first name ko change krna tha to
hmne email naam ka alg function bnaya but vo chl to jayga lkin encapsulation ki property nhi follow krega to
hmne fir DECORATOR(PROPERTY) ko chlaya jo ki alg se hi koe bhi argument dene se hi chnge krdega usko bahar ke bahar"""
class Employee:
    def __init__(self,fname, lname):
        self.fname = fname
        self.lname = lname
       #here the email is inside the constructor so that we have some problem to change the first name to agr mai ise ek function bnadu to shyd ye chljaye lets try
        # self.email = f"{fname}.{lname}@portal.com"    #here we can specify the instance so that wee ont pass any arguments in the constructor as well as in any instance

    def Explain(self):
        return f"This employee is {self.fname} {self.lname}"


 #agr mai cahhta hu ki isko email as an attribuute du or usko directly acces kr pauu to mai ek decorator ka use kruga
    @property
    def email(self):
        return f"{self.fname}.{self.lname}@portal.com"

tanu = Employee("Tanu","Chuahan")
manu = Employee("Manu","Chauhan")

# print(tanu.Explain())
#JBTK EK ATTRIBUTE THA BUT NOT CHANGABLEE DIRECT(CONSTRUCTOR KE ANDR THA) TO YE PRINT HUA
print(tanu.email)  #here it can print the email jbtk ye constructor ke andr tha but fir adress print krega function ka naaki functions property
print(manu.email)
#but if i want to change my first name the what should i do i have to specify it like
#JBTK TO FUNCTION THA YE PRINT HUA
# print(manu.email())   #ye wala email ka alg se function bnane ke baad ka hai
#YE CHANGE KRA TO AB SB FAIL HGYA CONSTRUCTOR KE ANDR KAAM NHI KREGA OR EMAIL() FUCNTION KO AISE PRINT KRAYE TO ENCAPSULATION KHTRE MAI TO HM ISE PROPERTY SE PRINT KREGE
manu.fname = "Dharmesh"
# print(manu.email)   #here it cannot change the name like this because it can take by the consttructor aand them print as a first name which already specify in the oobject so for changing it we can use propert decoratorS
# print(manu.email())

#DECORATOR lgane ke baad ye sb ab function nhi rhe to ab ye as property lenge email function ko class ki
print(manu.email)

"""maanlo mai email ko set krna caahta hu or jin jin attributes se vo bna hai unko bhi set krna cahhta hu email ko
 input du or vo atribute lekr changr kde use to hm setter ka use krte hai """


class Employee:
    def __init__(self,fname, lname):
        self.fname = fname
        self.lname = lname

    def Explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname == None or self.lname == None:  #but agr mai cahhta hu ki ye none return na krein to mai property ke andr condition lgaa dunga ki ye print kre kuch or vo na kre agr none ho to halaki mne khud delete kra hai deletor se fir bhi ye lgaaya
            return "Email not set please set it using setter"
        return f"{self.fname}.{self.lname}@portal.com is your email"
#agr email change hota hai to ye function setter hai jo ki change krdega
    @email.setter   #email is a attribute jiusko hum input lena cahhte hai o fir setter se set krdein
    def email(self, string):
        print("Setting now...")
        names = string.split("@")[0]   #list return krega tukde krke @ se aage ka argument or piche ka alg alg krdega or fir ye khudka 0 inddex bnjayga
        self.fname = names.split(".")[0]   #at 0 index split by "." and print first name
        self.lname = names.split(".")[1]   #at 1 index which is a list return by split "."

    # ab mai cahhta hu setteer ko delete krna to usko delete krne ke lioye mjhee ek deleter bnana pdega but OOPS mai generally delete nh krte hm set krdete hao none direct
    @email.deleter
    def email(self):
        print("Deleting now...")
        self.fname = None
        self.lname = None   #ye sbko delete krdena dono ko jo set kiye the setter ne

manu = Employee("Manu","Chauhan")
manu.fname = "Dharmesh"
# dekho ye mai upr instance ke nadr jakr bhi chnge kr skta  tha but us se ecapsulation ki property khrab hojati to ye ab mai aise direct na krke alg se kruga
#YE EDIT KREGA SETTER
manu.email = "this.that@portal.com"   #to ye attribute ko set krne ke liye hm setter bnate hi ki jis se ye direct bahar se hi change hojaye hme baar baar email naame ke fnctn ko chlane ki jrurt na pde
print(manu.email, manu.fname)   #ab isko hm direct bina kisi function ke calling kiye ek setter ki propertty se as an attribute work krega or andr se arguments pas krfdega hmein
#ab mai cahhta hu setteer ko delete krna to usko delete krne ke liye mjhee ek deleter bnana pdega
del manu.email
#ab agr mai print kruga to ye fname or last name none print krdega
print(manu.email)
#or delete krne ke baad agr mai waps ise set krke rum kruga to vo is baar ise set krlega setter ki mdt se
manu.email = "Manu.bhai@portal.com"  #yha run krne pr dkhayga setting noe then
print(manu.email)


#and getter is used for to acces of the private elements of the class by get_(var_name) which can get the private in any method
# like:-
class SampleClass:

    def __init__(self, a):
        ## private varibale or property in Python
        self.__a = a

    ## getter method to get the properties using an object
    def get_a(self):
        return self.__a

    ## setter method to change the value 'a' using an object
    def set_a(self, a):
        self.__a = a