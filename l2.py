e=[]
o=[]
a=[]
for i in range(1,101): 
    a.append(i)
    if i%2==0:
        e.append(i)
    else:
        o.append(i)    
print(a,'-full list')
print(e,'-even list')
print(o,'-odd list')