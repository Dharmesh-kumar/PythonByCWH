Khana=["roti","sabji","chawal"]
for item in Khana:
#for loop ke sath else tbhi chlta hai jb for loop ko koe break statement na mile or normally nd ho ya to list iterable khtm hojaye or ya to koe break statement miljaye
     print(item)   #agr mujhe yha break miljat to ye else mai jaata hi nhi

else:
    print("This for loop ended properly")

#we can use it  for searching a item in list
Khana = ["roti", "sabji", "chawal"]
for item in Khana:
# agr mujhe yha break miljat to ye else mai jaata hi nhi
      if item=="paratha":
          break
else:  #jo hmari list mai nhi hota to ye ayega agr hm kisiko search krarhe ho list ke andr
    print("This for loop ended properly")