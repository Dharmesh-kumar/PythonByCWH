#varibles scope
#global variable and local variable
l=10    #sarkaar ka paaisa             #global variable:-in this program every funcction is used by global variable
# and l is in the global scope which means koe chiz kha tk jaa skti vo khi se bhi program mai value access kr skti hai
def function1(n):
    l=5    #function personal variable   #local variable
    m=8     #personal paisa
    print(l,m)    #personal paisa print
    print(n, " i have printed")

function1("this is me")
print(l)     #sarkar ka paisa print
#sbse phle function apne variables use krega or unki value print krega uska global se koe lena dena nh hga but agr uske
# pass kuch nh hua to vo khudse apna global variable lelega

#the global variable access by local variable
l=10
def function1(n):
    m=8
    global l  # sir(function) apko l naam ke variable ko access krne ki anumati mil chuki hai
    l=l+45              # if  we can print l as inside the local variable the it doesn't take the value
    print(l,m)
    print(n, "i have printed")
function1("this is me")

# nested function
x=89     #if we add global var here then the global var at tanu function makes it 88
def Dharmesh():
    x=20
    def Tanu():
        global x   #the global var always check the value outside fron thee local var and calling the value first in the second function
        x=88       #here the global variable dont calling 88 because it print the local function variable dharmesh
    print("before calling function Dharmesh()", x)
    Tanu()
    print("after calling function Tanu()",x)
Dharmesh()
print(x)