def searcher():   #ye noral function nhai rehgya ab ye coroutines bngya kyki hmne yield bnaadiya jo ki on the fly gernerate krega jo bhi hm search krege string mai or ye yha kaaam krna suru krdega searcher function mai
    import time
    # some 4 seconds time consuming tasks
    book ="This is a book on how to be a billionare and millionare"   #reading this string
    time.sleep(4)    #yhqa tk 1 baar kaam krega or jitni baar mai isko value send kruga ye fir tym nhi lega niche chlane mai
#hmne ye function bnaya hai to abhi hm ise use krege jo ki ye fuynction run hga ek tym  mai or fir agr hm ise dobaa kuch print ya fir koe function bhi run krna caHte hai to aage ye niche ka run hga ise hi coroutiness kehte hai
    while True:   #an infinite loop for true jbtk ye chlta rhega generator
     #ye yiled ab text mais ntore hojayga or function chaalu hohi rkhka hai vo coroutines bnjayga
        text=  (yield)   #yha pr ise generator on time fly wala yield krke dedega after 4 seconds ke time pr
        if text in book:
            print("your text is in the book")
        else:
            print("your text is not in the book")

search = searcher()  #coroutine ka instance
print("Search started...")    #dekhna yha tym nhi lega kyki yha se start hga coroutine ab ispr  next lgane se phle aage bdhgne ke liye y tym lega 4 seconds ke delay ka or fir print krega aage
next(search)    #value send krne ke liye ise start krne pdega to next chlana pdega
print(type(search))
search.send(input("enter the word which you want to search: "))
search.close()
# search.send("manu")    #ye close hne ke baad kam nhi krega saari resources releasr krdi
"""USE:- jbn hmare fucnxtion main kuch aisi chize hai jinko initialize krne mai kaffi ttym lgta hai or vo ek bvaar initialize hojati hai to uske baad kaaam krta hai delay isiliye hai ki kuch bhi aisa kam jinme hmein generally tym lgta hai kuch bhi krne mai jaise machine learning ke models ko read krne ka tym
vo lga ye tym for ex jaisa uske bad while true ke baad chlta gya manlo function ka kaam khtm hua to ab ye saare resources releasr kena cahhtwe ho to bnd kro close se"""


def find_name():
    import time
    name="manu tanu rasha ira rimjhim ishu bhuvik mann vedang bhomik tinu sidhu chetan shree sidhi "
    time.sleep(3)


    while True:
        text= (yield )
        if text in name:
            print("You are family memmber son")
        else:
            print("You doesn't belongs to be here ")

names= find_name()
print("searching started...")
next(names)
names.send(input("Enter the name: ").lower())

