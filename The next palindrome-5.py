# palindrome:its us a string when reversed is equal to itself
# ex:- mom,616,10001
# you have to take a number as the input from the user you have to find the next palindrome correspondance to the number
# your input should be a number of test cases as the input and then take all the cases as input from the user
# input:
# 3
# 451
# 10
# 2133
#
# output:
# reverse palindrome of for 451 is 454
# reverse palindrome for 10 is 11
# reverse palindrome of 2133 is 2222

test_case=int(input("Enter the number of entries: "))
for i in range(test_case):
   num=int(input("Enter the number of the test case:"))
   while True:
             number=num
             num +=1
             str_num = str(number)
             if str_num==str_num[::-1]:
                 print(f"{str_num} is the palindrome")
                 break
             else:
                continue

# def next_palindrome(n):
#     n=n+1   # if number is already palindrome then print next of that palindrome
#     while not is_palindrome(n):
#         n+=1   # loop until number is palindrome
#     return n
# def is_palindrome(n):
#     return str(n)==str(n)[::-1]   # for checking the reverse of the number for making palindrome
#
#
# if __name__ == '__main__':
#
#        n=int(input("Enter the number of test cases: "))
#        numbers=[]
#        for i in range(n):
#               number= int(input("Enter the number: "))
#               numbers.append(number)
#        for i in range(n):
#               print(f"The next palindrome for {numbers[i]} is {next_palindrome(numbers[i])}")