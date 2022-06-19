#is and ==
# is:-  reference equality- Two referances refer to the same value(iska mtlb hai ki vo dono object hek hi hai)-khud brabr hniska mtlb is?
# ==:- value equality- Two objects have the smae value(agr mai kinhi 2 objects pr == chlata hu to un dono ki value barabr hai cahhe vo objects alg hi kyu na ho)- value brabr hai?

a=[6,4,"32"]
b=[6,4,"32"]
print(b is a)   #here  both a and have diffrent vriables so they cant br same(is) but they have the same value
print(a==b)    #here their value are the same so thats why it gave True
