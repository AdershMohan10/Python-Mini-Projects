l1=int(input("Enter 1st limit:"))
l2=int(input("Enter 2nd limit:"))
print(f"Prime numbers between {l1} and {l2} are:")
for n in range(l1,l2+1):
    if n>1:
        is_prime=True
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                is_prime=False
                break
        if is_prime:
            print(n)    
    

