import json  #JSON:- Java script object notation
#no comments and always in double quotes
#loads:- kisi bhi strings ko as an argument leta hai
#strings ke liye hai loads mai idhr json
data='{"var1":Manu,"var2":56}'
print(data)
parsed = json.loads(data)
print(parsed['var1'])   #here it can be decode into JSON so it can take key value pairs as string also otherwise we know string index must be integer but in jsion it can print value by parsed it

#load:- accepts the file object  ye kisi bhi object ko as an argument leta hai
with open("json_data.json","r") as content:
    print(json.load(content))
#dumps
data2={
    "channel_name":"LETS GET KNOW",
     "cars": ['bmw','audi R8','ferarri'],
     "fridge": ("roti",540),   #or jaise ki tuple ki value bhi print krdega jo ki nhi krni chiye thi
     "isbad" :  False      #jo ye hai ye jaise hki javascript mai small mai hota hai to vha ke liye ye error throw krdega
}
#dictionary to json compatible banne ke liye hm use krege is funciton ka
jscomp= json.dumps(data2)     #ab ye dumps krdega pura compatible bna dega
print(jscomp)
print(sorted(jscomp))


#sort_keys params in dumps:- value pairs ko sort krne ke kaam aata hai ye ek  true or false params leta hai or if we give param true:anmswe will be in alphabetical order if it false: answer wil;l be as it is form