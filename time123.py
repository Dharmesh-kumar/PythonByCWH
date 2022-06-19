import time
initial = time.time()

k=0
while(k<45):
    print("this is Dharmesh bhai")
    time.sleep(.2)                      #the function is sleep for 2 seconds betwween program
    k +=1
print("while loop ran in",time.time()-initial,"seconds")

initial2= time.time()
for i in range(45):
    print("this is Dharmesh bhai")

print("for loop ran in", time.time() - initial2, "seconds")

#while loop and for loop are working in the same time almost

localtime = time.asctime(time.localtime(time.time()))
print(localtime)
