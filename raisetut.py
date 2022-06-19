#built-in Exceptions
#raise:- Jb me kisi error ke baare mai pta ho or hm fir uske liye ek particular message print krna caahte hai to ye hga
#Exception in numeric
# a= input("What is your name")
#yha tk program run hga but agr hme pta hai ki is se aage jo bhi program hai vop jyada tym lene wala hai to jis se time bche or server pr load aane wala hai in 1000 lines ko na perform kre to raise use krte haia
# program phle hi rukjayga agr input koe number hua to vrna run krega
# if a.isnumeric():
#      raise Exception("numbers not allowed")   #ye time bcha lega age ka run hi ni krega yhi error throw krdega 1000 lines ka code valid hi nh hga aage
# print(f"hello {a}")
# #1000 lines of code take 1 hour for run


#Raise division error
# a= input("What is your name") #manlo a ko execute hne mai lgta hai 10 secnd
# b= input("How much do you earn")
# if int(b)==0:
#     raise ZeroDivisionError("b is o so stopped the program!")
# print(f"hello {a}")

#index Error- jb list choti ho or uske aage ka elements use krne ki kosis ki jaa rhi ho

#value Error:- Jb variable ka type shi ho but value galat paass hgyi ho
c= input("Enter your name")
try:
    print(a)
except Exception as e:
   if c=="manu":                  #naam pehle hi mna krdega ki ye baanned hn andr jaane se
        raise ValueError("Manu is not allowed")
   print("Exception handled")

#type error:- jb variable ka type wrong hga
 # print(sum(3+"4"))

# name error:- variable declaration ke pehle ki name use ho
# eg:- print(name)