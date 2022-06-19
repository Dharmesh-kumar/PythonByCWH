# modules from which python interpreter can work and the libraries are working
# import sklearn as sk                         # In global scope
# print(sk.__version__)

# ensamble is used for making decision by classifier
from sklearn.ensemble import RandomForestClassifier
print(RandomForestClassifier())       #randomforest classifier is a class which is used in the machine l

import file2
print(file2.a)
# or     work in both ways but import is way better than from because if there is another file with same var so there is formation of ambiguity
from file2 import a
print(a)

import file2
file2.printjoke("This is me")
# if we have to use the function from another files then we have to use it as import them from the file to file
# DON'T MAKE THE FILE NAME AS THE MODULE NAME BECAUSE IT CAN SEARCH THE MODULE AFTER YOU IMPORT IT THEN IT CAN CHECK IT OUT FROM THE DIRECTORY BUT IF FOUND THE DIRECTORY SAME SO  IT CANNOT WORK

