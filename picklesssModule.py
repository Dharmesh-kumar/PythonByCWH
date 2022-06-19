#pickle can be used as an security threat because if we can pickle a data in pyhton 3.3 version and unpickle it into python 3.6 or any versiuon so we r facing such issus so its not convinient to do it as it way
import pickle
#preservation krke rkh dena kisi bhi object ko
#hr chiz ek object hoti hai cahhe kuch bhi data download krne ho gya parsed krna ho gya or jo bhi hme sb kucvh krke ek list niklgi usme se or hm frquently  krne pdra hai to hm use jo bhio hmne parsed kiya hai ya kuch bhi function ka use iya usko hm
#aise hi dabbe mai pack krke rkh skte hai or we can say tha we should preserve that list in the file as pickle

#PICKLING A PYTHON OBJECT
# cars = ["Audi","BMW","Bughati","Lambo"]
#  # Ye list hai to mai is cars object ko store krke ek file mai rkh dunga or vo file mai isi module i mddt se open krke read krlunga jruri nhi ye list hi ho mai kisi bhi ppython ke type ke sath aisa kr skta hu
# file = "mycar.pkl"
#
# fileobj= open(file, 'wb')     #yw binary read krega mode binary file format rkhna pdega
# pickle.dump(cars, fileobj)     #dump jo hota hai vo 2 argumens leta hai 1- vo objecxt jo pack krna hai or dusra file objeect not particular object so we have to make a file object
# fileobj.close()

#De-pickle (how to get that object)
file = "mycar.pkl"
fileobj = open(file,'rb')
mycar = pickle.load(fileobj)   #ek file obj leta hai as an argument or return krta hai vo object
print(mycar)
print(type(mycar))
fileobj.close()

#pickle.loads =  un data ke liye hota haio jo bytes ke form mai rehte hai or we can say tht it can ake only bytes aobjects in their argument or string ho