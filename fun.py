#def add():
 #   return print('hello')
#a=add()
#print(a)

#def add2(a=0,b=0):
 #   print(a)
  #  print(b)
#add2(1,2)    

def fact(n):
    f=1
    for i in range(1,n+1):
        f*=i
    print(f)
n=int(input('Enter number:'))
print('Factorial is:')
fact(n)





