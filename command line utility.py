#software:- 1:- GUI  :-which provide features
 # ex:-python jaise ek software hai to hm  usme code likhkr apne hisab se usko bolr rhe hai ki ye comment krde jakrr to vo ye kaam kr dega jo ki  ek command line utikity ka hi example hai\
# if i want  to make a command line utility:- hm ise kisi bhi dusre software se read kr skte hai usime add kr skte hai
     # ClI:- command line interface
     # hm iska use vha krte hai jha hme lgta ki koe rpogram ryn krega bhi ya nhi to hm uska ek basic model bnalete alg se or use apne bde program mai import kra lete
import argparse
import sys      #for write in console

def calc(args):
    if args.o =='add':
        return args.x + args.y
    elif args.o == 'mul':
        return args.x * args.y
    elif args.o == 'sub':
        return args.x - args.y
    elif args.o == 'div':
        return args.x / args.y
    else:
        return "something went wrong"


if __name__ == '__main__':
    parser = argparse.ArgumentParser()    #argparse krega  or sath hu maia rgument ko parse krdega aage jake jo ki add krege avaarious arguments by direct
    parser.add_argument('--x',type=float,default=1.0,
                        help='This is a utility for calculation. please contact manu bhai')
    #ye jo aarguments apne andr lega yha isme x nam ya fir koe bhi hm varibale dal skte hai or fir uske baad konse type rkhna cahhte hm then uske baad koe bhi alue jo print ho bina kisi value ke enter kre vo default set kr skte then uske baad uske baaad agr help lena caahe to messg rpin ho
    parser.add_argument('--y', type=float, default=3.0,
                        help='This is a utility for calculation. please contact manu bhai')
#here default is add so botht he values are added with default and we have to choose if we want
    parser.add_argument('--o', type=str, default='add',
                        help='This is a utility for calculation. please contact manu bhai')

    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))   #STDOUT:- FOR OUT IN THE CONSOLE THIS ARGUMENT PARSE
    """sbse phle calc naam ka function jo hai vo args pas krega apne andr then uske baad co string mai bdl dega sbko or fir stdout jo hai vo sys ki 
     ek class hai jo use console mai lejakr write argument krdega usiki sath sb args ki sath jo hm krvana cahhte"""