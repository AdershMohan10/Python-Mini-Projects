class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self,otr):
        t1=self.m1 + otr.m1
        t2=self.m1 + otr.m2
        return(t1,t2)
    
    def __sub__(self,otr):
        t1=self.m1 - otr.m1
        t2=self.m1 - otr.m2
        return(t1,t2)
    
    def __mul__(self,otr):
        t1=self.m1 * otr.m1
        t2=self.m1 * otr.m2
        return(t1,t2)
    
    def __trudiv__(self,otr):
        t1=self.m1 / otr.m1
        t2=self.m1 / otr.m2
        return(t1,t2)



s1=Student(7,5)
s2=Student(5,6)

print(s1+s2)
print(s1-s2)
print(s1*s2)
print(s1/s2)
