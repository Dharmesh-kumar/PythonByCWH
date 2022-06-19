#ek strings mai se ek specific pattern ko nikalne ke liye:- aasan trika
import re
mystr= '''my family
 RAVINDER SINGH CHAUHAN  01335-248176
 DHARAMBATI CHAUHAN
 HARENDRA CHAUHAN    +91-9917892829
 SOHNI CHAUHAN       +91-9719466239
 JOGENDRA CHAUHAN    
 SARIKA CHAUHAN      +91-9811331299
 DHARMESH CHAUHAN    +91-9779006874
 
 PRIYANSHU CHAUHAN   +91-9045892829
 ADVIKA CHAUHAN    
 SHARANYA CHAUHAN
 aiiiii aaaa iiiii  aiaiaiai'''

# Normal way
# print(mystr.find("DHARMESH"))

# findall,search,split,sub,finditer
# 1-findall:- specific string matcheD hai unko uthakr string return kr deta hai
# 2- search:- ye match obj ko return krta hai
# 3- list:- split krdena alg alg lines ko

#raw string:- agr hm jaise \n print krte hai to ye print krta hai new line but agr hm print(r'\n' krege to ye print krega \n jo ki escape sequence character ko form nhi krta
# use:- regular expression mai raw string ka use krte hai Escaping nhi krni pdegi direct interpret krdega
# meta characters:- regular expressions mai lgane ke liye 2 treh ki sequences hoti hai
#normal searching by re module
# patt = re.compile(r'DHARMESH')
# matches=patt.finditer(mystr)
# for match in matches:
#     print(match)    #her eit can shows span of there string which means the indexes of the string from to up to
#     print(mystr[124:132])    #this is the span in which we get in the compiler on searching the word Dharmesh

# for complicated searching using metacharacter and special sequence:

# Meta characters:-
# patt = re.compile(r'.DH')          #. means for searching or all characters
# patt = re.compile(r'CHAUHAN$')   #chauhan word se end hua hui sltrings index return krega
# patt = re.compile(r'^my')        #my word se start hua hai vo bta dega position
# patt = re.compile(r'ai*')          # zero a or i dono jha bhi hnge vo return krdega unka index
# patt = re.compile(r'a*i*')          #zero ya kitne bhi a ho or i dono jha bhi hnge vo return krdega unka index
# patt = re.compile(r'ai+')          #a ho ya fir i one ya us se jyada ka return krdega unka index
# patt = re.compile(r'ai{2}')          #exactly a or jha 2 times i hai sirf vohi return krdega unka index
# patt = re.compile(r'(ai){2}')        #group of exactly (ai)both 2 times hai sirf vohi return krdega unka index
# patt = re.compile(r'ai{1}|t')        #ya to mujhe ek ai chiye ya fir t dono mai se koe bhi ho dede
# matches=patt.finditer(mystr)
# for match in matches:
#     print(match)

# special sequences
# patt= re.compile(r'\Amy')      #my se hi start hori hai to ye return krdega
# patt= re.compile(r'CHAUHAN\b')      #jha bhi chauhan se ending hori hai to vo ye print krdega
# matches=patt.finditer(mystr)
# for match in matches:
#     print(match)

#manlo mere pss kaii saare PNT type phone numbers hai to
# patt = re.compile(r'\d{5}-\d{6}')    #numbers search krega string ke andr phle \d jo ki numbers search krta hai 5 krega or fir jo ki split ho rkhka hai - se to uske baad mai aaage kaa execute krega
# matches= patt.finditer(mystr)
# for match in matches:
#     print(match)


#given astring with a lot of indian nykbers starting from +91 and return all the numbers
patt=re.compile(r'\W{1}91-\d{10}')
matches= patt.finditer(mystr)
for match in matches:
    print(match)