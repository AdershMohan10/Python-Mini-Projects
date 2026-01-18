class Student:
    age=15
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll

    def stname(self):
        print(self.name)

    def change(self):
        self.name='lalala' 

    @classmethod
    def changeage(cls):
        cls.age=17           

s2=Student('ababa',23)
s2.changeage()
print(s2.name)
print(s2.age)        