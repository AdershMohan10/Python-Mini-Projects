import time
mark=0

print('A.Which planet is known as The Red Planet?')
print('1.Venus\n2.Mars\n3.Jupiter\n')
stime=time.time()
ans1=int(input("Enter your answer:"))
etime=time.time()
if  etime-stime<=30 and ans1==2:
    mark+=1
else:
    mark=0
    print("Time up or Wrong answer")

print('B.What is the capital of Japan?')
print('1.Tokyo\n2.Osaka\n3.Kyoto\n')
stime=time.time()
ans2=int(input("Enter your answer:"))
etime=time.time()
if  etime-stime<=30 and ans2==1:
    mark+=1
else:
    mark=0
    print("Time up or Wrong answer")


print('C.Which data type is immutable in Python?')
print('1.List\n2.Dictionary\n3.Tuple\n')
stime=time.time()
ans3=int(input("Enter your answer:"))
etime=time.time()
if  etime-stime<=30 and ans3==3:
    mark+=1
else:
    mark=0
    print("Time up or Wrong answer")


print('Who developed the theory of relativity?')
print('1.Isaac Newton\n2.Albert Einstein\n3.Galileo Galilei\n')
stime=time.time()
ans4=int(input("Enter your answer:"))
etime=time.time()
if  etime-stime<=30 and ans4==2:
    mark+=1
else:
    mark=0
    print("Time up or Wrong answer")


print('What is the chemical symbol for gold?')
print('1.Au\n2.Ag\n3.Gd\n')
stime=time.time()
ans5=int(input("Enter your answer:"))
etime=time.time()
if  etime-stime<=30 and ans5==1:
    mark+=1
else:
    mark=0
    print("Time up or Wrong answer")
                    

print("\n\nTotal Marks:",mark)        