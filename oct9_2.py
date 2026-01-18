class Student:
    def __init__(self, name, roll, age):
        self.name = name
        self.roll = roll
        self.age = age

    def marks(self, m1, m2, m3, m4, m5):
       
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.m4 = m4
        self.m5 = m5

    def sum_total(self):
        self.s = self.m1 + self.m2 + self.m3 + self.m4 + self.m5
        print(f'Sum of Marks: {self.s}/250')

    def avg(self):
        self.av = self.s / 5
        print(f'Average: {self.av}')

    def percentage(self):
        self.prc = (self.s / 250) * 100
        print(f'Percentage: {self.prc}%')

    def details(self):
        print("\nStudent Details:")
        print(f'Name: {self.name}')
        print(f'Roll No: {self.roll}')
        print(f'Age: {self.age}')
        print(f'Sum of Marks: {self.s}/250')
        print(f'Average: {self.av}')
        print(f'Percentage: {self.prc}%')



s1 = Student('ababa', 10, 22)


s1.marks(45, 38, 41, 48, 35)


s1.sum_total()
s1.avg()
s1.percentage()


s1.details()
