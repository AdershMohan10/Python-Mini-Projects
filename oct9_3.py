class Person1:
    def __init__(self):
        pass
    def read(self):
        print('p1 can read')
    def write(self):
        print('p1 can write')

class Person2(Person1):
    def __init__(self):
        pass
    def jump(self):
        print('can jump')
    def run(self):
        print('can run')

class Person3(Person2):
    def __init__(self):
        pass
    def fly(self):
        print('can fly')
    def swim(self):
        print('can swim')

class Person4(Person3):
    def __init__(self):
        pass
    def sleep(self):
        print('can sleep')
    def eat(self):
        print('can eat')

p4=Person4()
p4.read()
p4.write()
p4.jump()
p4.run()
p4.fly()
p4.swim()
p4.sleep()
p4.eat()

