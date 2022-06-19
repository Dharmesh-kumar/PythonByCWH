#if you have to print set
s=set()
print(type(s))
l=[1,2,3,4]
s_from_list=set[l]      #set print from the list typecasting
print(s_from_list)
print(type(s_from_list))

 #for adding element in set
 #what is the purpose of the set for making unique datatype? its work same as the list because it retain unique values
s.add(1)
s.add(2)
print(s)    #for print two elements in the set

s.add(1)
s.add(2)
s.union({1,2})  #we have the seperate union fuction for the sets
print(s)

s.add(1)
s.add(2)
s1=s.union({1,2,3})  #assign seperate variable to store another
print(s,s1)
s1=s.intersection({1,2,3})   #for print the intersection the set
print(s,s1)
print(len(s))          #for print the length of the set
print(len(s1))         #for print length after intersection
print(type(s1))        #for print type after intersection
print(min(s))          #for print minimum value from the sset
print(max(s1))         #to print the max value from the set

s.add(1)            #to print the difference of the sets
s.add(2)
s1=s.difference({2,3})
print(s1)
#or method for diffrence if we have to find set then weh should compare the both subsets is written as a list
l={1,2,3}
s=l.difference({2,3})
print(s)
print(type(s))

s.add(1)
s.add(2)
s1={1,2,3}
print(s.isdisjoint(s1))     #checck weather the elements in the s or s1 is same or not if same joint or not same disjoint

s={1,2,3}
s.remove(2)      #remove element from the particular set
s1={4,5,6}
print(s,s1)
