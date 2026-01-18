n=int(input("Enter a number:"))
r=0
while n>0:
    b=n%10
    r=r*10+b
    n=n//10
print(f"rev is {r}")    
