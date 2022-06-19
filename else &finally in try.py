f1 = open("manu.txt")
try:
     f = open("docs1.txt")  # if file not exist then go to except then vo print hga uske baad mai to finally mai jakr vo tasks perform krega hi krega
     f.close()
# except Exception as e:
#     print(e)
#alg alg type ke error aane pr
except EOFError as e:  #agr end of file eroor aajaye to
    print("EOF error aa gya hai",e)
except IOError as e:
    print("I/O error aa gya hai",e)
#else:-except agr run nhi hota hai to else mai run hgi
else:
    print("this will run only if except is not running")
# finally:- jb hum cahhte hai ki jo bhi hmne open kiya hai or ya mai khu kin jaise ki hmne file open ki hai cahhe vo exist krein ya na krein but vo kuch na kuch kaam kregi hi
finally:   #cahhe exception occur kre cahhe na kre ye to hona hi hai try krne ke baad run ho ya na ho ye f.close hga hiu hga
    print("Run this anyway")
    f1.close()
    # f.close()

print("important stuff")
