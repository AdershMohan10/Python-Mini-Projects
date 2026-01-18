a=[100,2,3,5,-98,3,4,5,-999,3,34]
largest=0
smallest=0
for i in a:
        if i>largest:
            largest=i
        elif i<smallest:
            smallest=i
print(largest,smallest)            
