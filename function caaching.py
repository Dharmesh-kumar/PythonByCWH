#USE:- similar calls ko repeat krne mai jo tym lgta hai vo bcha leta hai
#sbse phle main functools se lru_cache ko cll kraya use bola ki meri pichli 3 cll ko save krke rkhna kyki mai baar baar use run nhi krna cahhta time.sleep sirf dikhane ke liye likha tha delay dikhakr ki delay hga ab wait nhi krna pdega ye lgakr but actuall mai
# ye time.sleep nhi hga vo legfa ek baar apna tym or tym lene ke baaad jb hm use nxt ym print krege to vo apni memory mai store krlega as we set maxsize=3 mtlb 3 value save hojaygi

from functools import lru_cache
import time
#decortator
@lru_cache(maxsize=3)      #maxsize jo hai vo apki memopry ko utna hi khayga baar baar ye program run krne ke liye ek baar tym lene ke baad fir dobara  lega hi nhi to hm baar baaar yha se use print kra skte jiska max siZze agr hm n ke base pr rkhke to vo n seconds tym lega then uske baad khi tym nhi lega
#abhi maxsize=3 3 value ko lene ke capable hai
def some_work(n):
#sometasks taking n seconds
  time.sleep(n)
  return n

if __name__ =='__main__':
    print("Now running some  work")
    some_work(3)   #or yha bhi lega kyki 3 max size hn to 3 seconds ka lega hi ty, but agr vha max size 3 hi rhe or hm isme or jyada functioons run kraye to vo
  #to ye ab in niche ke 3 mai hi apna max size lelega or ye value store krlega kyki ek baar yha tym lega hi
    some_work(1)
    some_work(6)
    some_work(9)   #puri 9 min tk ye tym lega or run hota rhega andr store hga but max size uska 3 hi hai to ye yha tk 3 valuedss ko store krega
    print("done...calling again")

    # ye waps iske niche delay ayega kyki vo pichli sirf 3 value ko hi store kr payga isiliye agr hm max size ka space bdha dein to vo inhe bhi save krlega ek baar hi 9 seconds ke time interval mai hi fir isme tym nhi lega but space km hai to vo yha bhi tym lega
    some_work(3)    #ye function turnt run krjayga ab lru_cache ki vjhse but max size uska 3 hai yha to tym lega hi voonly 3 second ka hi
    print("called again")

#mmanlo hmein koe internet se koe webpage access krna hai to ye ek baar run hga fir usjke baad ye vha se lekr ayega or apna tym lrega proper or fir lene ke baad ye apni memory mai save krlega jis se ki jb bhi ap us function ko cll krein to vo vha se uthakr durect apko print krke dikha de use
# waps vo same kaam krne mai jo tym lgg rha tha vo ab dobara na lge ye hota haai caching in python
# but pyhton mai hm ise qye jo kaam hai save krne wala hai use hi de skte krne ka

from functools import lru_cache
import time

@lru_cache(maxsize=int(input("enter the size which you want to store your details: ")))
def take_time():
    time.sleep(3)


if __name__=='__main__':
    print("My name is manu chauhan")
    take_time()
    print("father name is Mr.Harendra kumar")
    take_time()
    print("mother's name is soniya chauhan")