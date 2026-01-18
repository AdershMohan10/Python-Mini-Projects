class Chicken:
    def __init__(self):
        pass

    def walk(self):
        print('Chick can walk')
    
    def fly(self):
        print('Chick can fly')

class Duck:
    def __init__(self):
        pass
    
    def walk(self):
        print("duck can walk")
    
    def quack(self):
        print('duck can quack')

class Farmer:
    def __init__(self):
        pass

    def catch_bird(self,bird):
        bird.quack()

chick=Chicken()
duck=Duck()
farm=Farmer()
farm.catch_bird(duck)                   