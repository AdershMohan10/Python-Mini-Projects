n=int(input("Enter a number:"))
a=len(str(n))
for i in range(0,n+1):
    for j in range(0,n+1):
        if (i**a)+(j**a)==n:
            print(f"{n} is armstrong!")
        else:
            print(f"{n} is not armstrong!")
                
