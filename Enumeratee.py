#suppose, here is the list which we print and then if we want to delete something from it
#if we know where is the item in the list
l1=["bhindi","aalo","chopsticks","chowmein"]
print(f"this is the list {l1}")
for items in l1:
  a=input("enter the food which you want to delete: ")
  l1.remove(a)
  print(l1)
# or
l1=["bhindi","aalo","chopsticks","chowmein"]
del l1[1]
print(l1)

#but we don't know where is the item
l1=["bhindi","aalo","chopsticks","chowmein"]
i=1
for item in l1:
    if i%2 != 0:
        print(f"please buy only these {item}")
    i +=1
#but if we want to short this process for delete we use Enumurate
l1=["bhindi","aalo","chopsticks","chowmein"]
for index, item in enumerate(l1):       #enumurate can give both index(i) and item at the same syntax
    if index%2==0:           #here index starts from 0 in the list so due to enumurate
# because we need bhindi and chopstick
        print(f"please buy only these {item}")