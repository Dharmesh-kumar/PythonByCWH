#modules in python
import random
#modules and sub modules access by import and we have an access of the functions into it
random_number = random.randint(0,1)    #generate raandom number which is a function inside the random module
print(random_number)
rand=random.random() * 100  #here module ke andr ek random name ka function hai
print(rand)

lst=["Star plus","DD1","Aaj Tak","Lets get know"]
choice=random.choice(lst)
print(choice)

# for download module go to terminal in python then use pip install module name
