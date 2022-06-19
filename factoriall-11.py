
def fact(number):
    if number==0 or number==1:
        return 1
    else:
        return number * (fact(number-1))    #recursion limitation that canno reccur the biggest nu,mmber by the reverse which can give memory worror for the maimum recuyrsion
def facttrailzeros(number):
        # fac= fact(number)
        # print(fac)
        # count=0
        # while fac%10==0:
        #     count=count-1
        #     fac= fac/10
        # return count
     count=0
     i=5
     # 100!=100//5 + 100//5*5
     while number//i !=0:
           count += int(number/i)
           i=i+5
     return count

if __name__ == '__main__':
    # number= int(input("Enter the number: "))
    # fac= fact(number)
    # print(f"The factorial of the number is {fac}")
    print(facttrailzeros(int(input("Enter the number: "))))
