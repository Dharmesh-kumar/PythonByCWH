#curency converter:-
with open('currencydata.txt') as f:
    lines=f.readlines()
currencyDict={}
for line in lines:
    parsed= line.split("\t")
    currencyDict[parsed[0]] = parsed[1]
# print(currencyDict)

amount=int(input("Enter the amount: "))
print("Enter the name of the currency you want to convert this amount to? Available options: ")
[print(item) for item in currencyDict.keys()]
currency= input("Enter the one of these values: ")
print(f"{amount}  {currency} is equal to {amount + float(currencyDict[currency])} {currency}")