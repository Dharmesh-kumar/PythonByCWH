class student:
    pass          #we can use pass where we shouldn't want to execute the program here so that it can pass to there,after
harry = student()        #these are the objects in the class
manu = student()        #class can never be empty it hass some blueprint for making program easy

harry.name ="Harry"     #these are the variables in the instance or in object
harry.std= 12
harry.section=1
manu.subjects=["hindi","english","maths"]
print(harry.name,harry.std,manu.subjects)
