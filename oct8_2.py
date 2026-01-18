class Person:
    def __init__(self,name,byear,age=0):
        self.name=name
        self.byear=byear
        self.age=age

    def calc_age(self):
        self.age=2025-self.byear

p1=Person('adersh',2003) 
p1.calc_age()
print(p1.age)           
        
    