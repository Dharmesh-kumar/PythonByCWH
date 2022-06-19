#kbhi bhi HTTP requests bhjne ke liye hm program ke beech maai ise use krte hai
#get request:- kisi bhi url ke content lekr vo hm apn program mai laan cahh rhe hai vo URL hai
import requests
r= requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
print(r.text)   #yha pr ajayga sb likha hua basically us url ka source code aajayga yha pr
print(r.status_code)
#jo get req hota hai vo url apni browwser history mai save krleta hai to agr hm cahhte hai ki vo save na kre to hm
# post reequests ka use krte hai kyki ye passwrds vgehra url mai nhi bhej skte to hm pos se bhejte hai

# #post req:- jiska API end point(URL) hota hai or hmn uski sath sath data bhejna pdta hai
# url= "www.something.com"   #manlo ki koe particular website hai agr hm,ne use ek data bheja
# data={
#     "p1":4,     #jaise ki ye dono params hai to ye jakr vha data unhe show krege or vo is se match krega apne database mai
#     "p2":8
# }
# #fir jo response ayega use hm apne python program mai le kste hai requests.posts se
# r2= requests.post(url=url,data=data)   #kyki jo url ya fir data hai vo post function lee rha hai to ise aisa krne se hmeinm ek response milega
#status code:-  all the status printed on print a specific code

