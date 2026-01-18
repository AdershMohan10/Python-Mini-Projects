class A:
    def __init__(self):
        pass
    def hello(self):
        print('hey A')

class B(A):
    def __init__(self):
        pass
    def hello(self):
        print('hey B')

s1=B()
s1.hello()