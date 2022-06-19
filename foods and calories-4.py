# you visit a restaurant called manu_Da_Dabha and food items in this restaurant are sorted based on their amount containing the calories
# you have to reverse the list of thee food items :
# 1-inbuilt method of python
# 2-slicing trick[::-1]
# 3-swapping first element with last one an second element with last one and soo on...
# then check al the methods which returns the same list
#
# input: take list as the input form the user [5,4,1]
# output: ex:1- [1,4,5]
#  2- [1,4,5]
#  3- [1,4,5]

print("Hy welcome to the MANU_DA_DHABA \n--Here you have the menu on the basis of the calories-- ")
n=int(input("Enter the size of the list: "))
menu=list(map(int, input("enter the amount of calories in the food items you want to reverse enter with comma(,): ").strip().split(",")))[:n]

#1- method
reverse1= menu[:]
reverse1.reverse()
print("The reverse of the list by method 1: {}".format(reverse1))

#2-method
reverse2=menu[:]
a=(reverse2[::-1])
print("The reverse of the list by method 2: {}".format(a))

#3-method
reverse3=menu[:]
for i in range(len(reverse3)//2):   #here divide by 2 is because list ke andr jo i hai vo half tk chla hjayga thenm uske baad vo jb half tk phuch jayga to waps se yehi same sequence chlani suru krdega to jiski vjhse vo list ko waps ulta kr dega to isiliye //2 krbna pdega jo ki integer output dega or purilist ka
       reverse3[i],reverse3[len(reverse3)-i-1]=reverse3[len(reverse3)-i-1],reverse3[i]
print(f"The reversed of the list by method 3: {reverse3}")