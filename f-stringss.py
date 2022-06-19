#F strings
#string formating: insert a var in the string
import math
me="Dharmesh"
a1=3
#a="this is me %s %s"%(me,a1)     #int his method the string have to input limited var
a="this is {0}  {1}"
#here this is tuple which cannot change the value and print the argument position in string
b=a.format(me ,a1)     #this is also working on the same concept to enter the string
print(b)

#concept of F(ast) strings
a=f"This is {me} {a1} {4*65} {math.cos(65)}"   #here you can use any expression and it worked by taking any python expression
print(a)

import time
second=time.process_time()
a=f"this is a result time for print {[second]} time "
print(a)
