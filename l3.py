x=[1,1,2,3,4,2,3,4,5,6,7,5,6,7]
v=[]
for i in x:
    if i not in v:
        v.append(i)
print(v)        