#UCI ML REPOSITORY
import pickle
import requests

# url = 'https://archieve.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
# iris_pkl_file = "Iris_data.pkl"
#
# def fetch_data(url):
#     mydata = requests.get(url)
#     with open("iris_data.txt","w") as f:
#          f.writelines(mydata.text)
#     with open("iris_data.txt") as f:
#         iris_contents =  f.readlines()
#     return iris_contents
#
# iris_list =[]
# for line in fetch_data(url):
#     iris_list.append([line.replace("\n","")])
#
# #pickling the object
# with open(iris_pkl_file,"wb") as fileobj:
#     pickle.dump(iris_list, fileobj)
#     fileobj.close()
#
# #de-pickle
with open("iris_pkl_file", "rb") as fileobj:
    mystr = pickle.load(fileobj)
    fileobj.close()

print("IRIS DATA")
for item in mystr:
    print(item, "\n",end= "")
print("No of items is: ",len(mystr))





data = requests.get("https://archieve.ics.uci.edu/ml/machine-learning-databases/iris/iris.data").text
print(data)
#automatically list bnjaygi
# l1=data.split("\n")    or for comprehension
# print(l1)
#list of list
l2=[item for item in data.split("\n") if len(item)!=0]   #not equal to zero is because you wont get any item empty in list
print(l2)

with open("myiris.pkl","wb") as f:
    pickle.dump(l2, f)
with open("myiris.pkl","rb") as f:
    pickle.load(f)