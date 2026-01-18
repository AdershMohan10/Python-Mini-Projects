name=(input("Enter a name:"))
for i in range(0,len(name)):
    if name[i] in 'aeiou':
        print(f"{name[i]} at position {i}")
    