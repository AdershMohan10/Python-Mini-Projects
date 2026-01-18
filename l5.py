z=[11,12,13,14,15,16,17,18,19,20,21]
a=[]
b=[]
mid=len(z)//2
for i in range(len(z)):
    if i<=mid:
        a.append(z[i])
    else:
        b.append(z[i])      
print(a)
print(b)            
