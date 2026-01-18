x=int(input("Enter a number:"))
org=x
r=0
while x>0:
    b=x%10
    r=r*10+b
    x=x//10
if r==org:
    print("true")
else:
    print("false") 
        