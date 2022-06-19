a = int(input())
b = int(input())
c = int(input())
e = []
for i in range(c):
    d = int(input())
    e.append(d)
e.sort()
print(e)
for ele in range(0,len(e)):



# def prize(L):
#     e = []
#     C = 4
#     for x in L:
#         for y in L:
#             if x != y and x + y == C and (y, x) not in e:
#                 e.append((x, y))
#
#     # Return list tuples that add to constant
#     return e


#