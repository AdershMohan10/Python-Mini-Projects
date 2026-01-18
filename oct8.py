#class myCar:
 #   def __init__(self):
  #      self.name='swift'
   #     self.color='red'

#    def start(self):
 #      print('car starts')

#car1=myCar()
#car2=myCar()  
#print(car1.name)
#print(car1.color)


class Car:

    def __init__(self,n,c):
        self.name=n
        self.color=c
        

    def start(self):
        print(f'{self.name} Start car')

    def stop(self):
        print(f'{self.name} Stop car')    

    def compare(self,otr):
        print(self.name)
        print(otr.name)


c1=Car('swift',2019)
c2=Car('m800',2024)
c1.compare(c2)
c2.compare(c1)

#print(c1.name)
#print(c1.color)
#c1.start()
#c1.stop()

#c2=Car('brezza','red')
#print(c2.name)
#print(c2.color) 
#c2.start()
#c2.stop()        

 