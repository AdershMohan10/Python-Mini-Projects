class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def reset(self):
        self.move(0,0)

    def move(self,a,b):
        self.x=a
        self.y=b

    def xmove(self,a):
        self.x=a

    def ymove(self,b):
        self.y=b

    

p1=Point(3,4)
print(p1.x,p1.y)
p1.reset()
print(p1.x,p1.y)
p1.move(7,8)
print(p1.x,p1.y)
