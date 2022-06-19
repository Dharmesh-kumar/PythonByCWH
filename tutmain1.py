def printhar(str):
    return f"Ye string Dharmesh ko dede thakur {str}"

def add(num1, num2):
    return num1 + num2 +5     #A function which can print wrong addition beacuse it add with 5 already in the function cannot seen by the user

# here is the problem,if we import this file from anywhere then it can also execute same content with all functions
# if we want to fetch the function from this file at anywhere in the program so we faced some issue like it can print all the functions at that program
# so we have to print it in the main so that it can fetch only particular function

print("and the name is",__name__)  #here it is shown that name is the file name from which program is execute
if __name__ == '__main__':    #if value of name=main then execute otherwise not(agr name ki value main hai to ye print kro niche ke programs)
   print(printhar("Dharmesh1"))  #example for same file program
   o =add(4,6)
   print(o)
