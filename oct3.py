#import math
import time
#print(math.factorial(5))
#print(math.sqrt(49))
#a=9.7
#b=math.floor(a)
#print(b)
#print(time.ctime())
a=time.time()
for i in range(1,5):
    print(i)
    time.sleep(1)
b=time.time()
print(a)
print(b)
print(b-a)    