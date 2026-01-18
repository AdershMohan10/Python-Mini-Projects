#def addz(*args):
 #   s=0
  #  for i in args:
   #     s+=i
  #  return s
#print(addz(1,2,3))

def fullname(**kwargs):
    f=''
    for i in kwargs:
        f=f+kwargs[i]+' '
    return f
print(fullname(fname='rob',mname='dow',lname='jr',sname='lala'))    