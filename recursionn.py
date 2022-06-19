#recusrion: function ke andr fucntion ka use krna
def print2(str1):
    print("this is " + str1)
print2("Dharmesh")


# n!= n* n-1 * n-2 * n-3.............1
# n!= n * (n-1)!
#factorial using iterative method
def factorial_iterative(n):
    """
        :param n:     #integer
        :return:      n* n-1 * n-2 * n-3..............1
        """
    fac=1
    for i in range(n):        #i start from 0 to (n-1)
        fac = fac * (i+1)     #i ko 0 se multiply na kre or jaye 1 se ekr n-1 tk
    return fac


number = int(input("Enter the number: "))
print(factorial_iterative(number),":factorial using iterative function")


def factorial_recursive(n):
    """
        :param n:     #integer
        :return:      n* n-1 * n-2 * n-3..............1
        """
    if n==1 or n==0:
        return 1
    else:
        return n * factorial_recursive(n-1)
number = int(input("Enter the number: "))
print(factorial_recursive(number))

#fabonacci funtion
def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

number = int(input("Enter the number: "))
print(fibonacci(number))


