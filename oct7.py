#file1=open('hello.txt','r')
#for i in file1.readlines():
 #   print(i)
#print(file1.readlines())
#file1.close()

#file2=open('bye.txt','w')
#file2.write('welcome t0 kochi')
#file2.close()

#file3=open('bye.txt','a')
#file3.write('hello\n')
#file3.close()


path="C:\\Users\\Dell\\Desktop\\python september\\bye.txt"

with open(path,'r') as file4:
    print(file4.read())
