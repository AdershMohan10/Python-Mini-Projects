a='hello good morning nice to meet you'
b=[]
word=''
for i in a:
    if i !=' ':
        word+=i
    else:
        b.append(word)
        word=''    
b.append(word)        
print(b)    

    