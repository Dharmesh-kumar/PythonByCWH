#*args and **kwargs
#IMPORTANT:- at the function we have to follow pattern as (normal,*args,**kwargs) fro function calling the arguments
def function_name_print(a, b ,c ,d,e):
    print(a,b,c,d,e)

function_name_print("Dharmesh","Harry","Rohan","tanu","Shivam")

#if we want to add a name in the function and print it without add a var in function so we used aargs
def funargss(normal,*args,**kwargs):       #the elements from the *har is passed here as a tuple so that the value of the function is not change
    print(normal)
    for item in args:     #convention as the name as args any name(we can used args as any name it can work as args)
     print(item)
    print("\nNow i would like to introduce some of our heroes")
    for key, value in kwargs.items():
        print(f"{key} is a {value}")

normal ="this is name"
har = ["Dharmesh","Harry","Rohan","tanu","Shivam"]    #no matter it is list or tuple it can go in function as a tuple
kw={"Rohan":"Monitor","Dharmesh":"Fitness Instructor","tanu":"Buisnessman"}
kw.update({"Shivam":"cook"})
funargss(normal,*har,**kw)

