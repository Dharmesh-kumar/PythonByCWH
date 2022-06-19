# you are given a list which contains some numbers ,you have to print a list of next palidntrome only if if thew number is less than 10
#     otherwise you will print the
# print(number)

# input:
# [1,6,87,43]
# output:
# [1,6,88,44]

def next_palindrome(n):
    n=n+1   # if number is already palindrome then print next of that palindrome
    while not is_palindrome(n):
            n+=1   # loop until number is palindrome
    return n
def is_palindrome(n): return str(n)==str(n)[::-1]   # for checking the reverse of the number for making palindrome

if __name__ == '__main__':

       n=int(input("Enter the number of test cases: "))
       numbers=[]
       for i in range(n):
              number= int(input("Enter the number: "))
              numbers.append(number)
       for i in range(n):
           if numbers[i]<=10:
               print(f"\"{numbers[i]}\" this is not a valid number enter the number greater than 10")
           else:  print(f"The next palindrome for {numbers[i]} is {next_palindrome(numbers[i])}")


#OR
# test_case=int(input("Enter the number of entries: "))
# for i in range(test_case):
#    num=int(input("Enter the number of the test case:"))
#    while True:
#          if num<=10:
#           print("Entered value must b greater than 10")
#           break
#          else:
#              number=num
#              num +=1
#              str_num = str(number)
#              if str_num==str_num[::-1]:
#                  print(f"{str_num} is the palindrome")
#                  break
#              else:
#                 continue
