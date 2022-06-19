#Overriding concept of class
""" first :- instance variable khojega
    then :- class check krega usme agr nhi hua to uski inherit mai jhake lega
    then :- vha milgya to print krega sbse phle instance or agr hm htadein vha se instance
      fir:- vo class B ka hi classvar1 print krega or agr vo bhi htade to fir to class A ka hi print krna pdega """

class A:
    classvar1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "I am inside class A's Constructor"
        self.classvar1 = "Instance var in class A"       #it can be printed because it can search instance variable first them the other name by it

class B(A):
    classvar1 = "I m in class B"   #ye override hgya lkin fir bhi vo instance variable check krega sbse phle jakr kyki instance mai hi sb value store hoti hai to isiliye

a=A()
b=B()
#agr mai ye print kruga b.classvar1 to sbse phle vo jayga class B mai or dekhega kya koe instance variable hai agr nhi hua to A mai jakr dekhega or print krdega
print(b.classvar1)   #here it can access the variable inmside the class A by B with inherit

#constructor overrride and super() function which solve override problem
class A:
    classvar1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "I am inside class A's Constructor"
        self.classvar1 = "Instance var in class A"
        self.special = "Special"
class B(A):
    classvar1 = "I m in class B"   #uske instance varible ko htane ke baad mai ye print hga kyki upr sb override ho chuka hga instace variable A class ka
    def __init__(self):
        super().__init__()  #ye print krdega variable  iska mtlb hai ki super() class ka constructor calling kradi particular ya fir ab kuch bhi vha se cll krwale agr niche wale mai nhi hai to
        #kyki override krane ke baad constructor class B ka hi sb instances lega agr hm upr wale dene ki kosis krein to error dedega kyki uske pass hai hi ni
    #abhi tk hmne ise override kradiya tha but agr hmein chiye ki print ho upr wale class ka vinstance variable to
        self.var1 = "I am inside class B's Constructor"
        self.classvar1 = "Instance var in class B"  #abhi to ye hai yha pr iska instance variable class b ka to yehi print krega or agr ye na ho to ye class b ka classvar1 hi print krega kyki8 ye constructor override krliya gya hai upr se ab isko hm use ni kr skte class A mai jbtk override nhi hua tha tbtk hojata but ab nhi hga
# ek baar jo chiz override hgyi vo waps run nhi hogi!
#but agr mai cahhta hu ki dono ke constructor print krein kyk dono jruri hai to vha pr hm super use krte hai
# a=A()
b=B()
#ab hm A class ke constructor mai kuch bhi ho use direct call kra skte by super()
print(b.special, b.var1 ,b.classvar1)  #here special from class A cy super function and var1,classvar1 are availiable in classs B so it can print them from there