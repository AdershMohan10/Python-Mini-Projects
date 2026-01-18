#def hello():
 #   print('adersh')
 #   return hello()
#hello()

#def tozero(n):
#    if n==0:
#        return 0
#    return n+tozero(n-1)
#print(tozero(3))

def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(5))
