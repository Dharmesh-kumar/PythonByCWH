#break and continue
#while loop
i =0
while(True):      #while 1 or while true is a loop which always working upto the limit
      print(i+1,end=" ")      #so it is print endless if we print only i but
      i = i + 1
      if (i==45):     #if we want to stop it at somewhere so wee have to specify it
          break        #yha pr aakr rukega

print(" ")     #this command for print used for clear the input
#what if the condition is not true then execute continue statement
i=0
while(True):
    if i+1<5:
        i = i + 1
        continue    #continue tk phuchega fir toot jayga waps upr hr condition pr check krega
    print(i+1,end=" ")
    if(i==44):
       break     #break from the loop
    i = i + 1
print(" ")
#enter the number which is greater than 100 and print the numbers
while(True):
    i = int(input("enter the number: "))
    if i<100:
        print("try again")
    elif i==100:
        print("you enter a number equals to 100")
        continue
    else:
        print("you entered a number greater than 100")
        break



