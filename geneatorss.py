""""
Iterable -  __iter__() or __getitem__() if we use these method on the object so they can give iterable (sbse phle ye chlega or ye interr krna suru krdena then
interator - __next()  (mai uspr next next krta rhuga object pr to vo aagfe chlta rhega nxt nxt krte hue then it can give next item
interation - agr ahhhta ki kisi python object ko traverse kruy ex:-list,string
or wee cann acess it in for loop is working or not that thwe object is itrable or not
"""
# yield hme sidhi value detaa hai bina kisi execution process ke dikhaye direct pause krke dedega or return terminate krdega internal process kro krta rhega choorta rhega
# generators:- these are the type of iterators of which we can only one time iterate not next to next only one tym formes(ye jo hoter hai ye on the fly value ko generate krte hai)
# maanlo jaise ki eek numberr hn vo bhi bda hai to vo jaisse hme on time hi kuch print krna ho jis se hmari ram bchi rhe mai nhi cahhta ki koe is se bhi bda numbr mai apni memory mai save krke rkhlu or system ko slow krlu
# so mai ek genrator bna lunga jo numbers ko generate krne ke capble hai bs maine bnakr rkhliya jb mjhe chiye hga tb krlunga
def gen(n):
     for i in range(n):
         yield i    #ye on the fly generate krega values or return ni krega jb mujhe jrurt hgi tb leluga isme se numbr
g= gen(3)    #it is a generator
# print(g)
# ye sirf rhega andr program mai reguular methods mai list bnata jo pura chlaygi or print krti rhei nhi ! mai kbhi bhi isme se numbr le skta hu koe bhi bina puri list ya kuch bhi numbr ko iterate kre sirf ek tym pr hi miljayga jb bhi mjhe chiye rhega
#ab hm jitni bar next print krege to ye interate hga baaki procewss show hi ni krega
print(g.__next__())
print(g.__next__())
print(g.__next__())   #ye hmne iterator lgaiya to ye dikhayga process
# print(g.__next__())   #ye ab yha error dedega to ise baar barr iterate krne kee liye for loop ka use krte hai hum jis se rukjaye vhi apne ap vewn in generator
#or  hm ise for loop se bhi kr skte the kyki for loop stop inteeration ko handle kr lete hai ot jaise hi generator khtm hojata hai to ye close hpjata hai ap
# for i in g:
#      print(i)

m="manu"   #int object is not iterable by iter function because isme __iter__ objet define nhi hota hai int ke liye
ier = iter(m)
# print(ier.__next__())
# print(ier.__next__())
# print(ier.__next__())
# print(ier.__next__())
print(next(ier))
print(next(ier))
print(next(ier))
print(next(ier))


#1-method
# for c in m:
#     print(c)



#FIBONACCI SERIES IN GENERATOR

def fab(n):
    a,b =0,1
    for i in range(n):
        yield
        a,b=a,a+b
# print(next(fab(a)))
g=fab(int(input("enterr the number: ")))
print(g.__next__())
print(g.__next__())
print(g.__next__())
# print(fab))))
# print(next(g))
