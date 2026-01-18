n=int(input("Enter a number:"))
is_prime= True
if n==1:
   is_prime=False
else:   
    i=2
    while i<n:
        if n%i ==0:
            is_prime==False
            break
        i=i+1
if is_prime:        
    print("prime")    
else:
    print(" not prime")