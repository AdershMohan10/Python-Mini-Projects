class Queue:
    def __init__(self):
        self.elements=[]

    def enqueue(self,value):
        self.elements.append(value)

    def dequeue(self):
        if not self.is_empty():
            self.elements.pop(0)
        else:
            print('queue is empty')

    def is_empty(self):
        if len(self.elements)==0:
            return True

    def peek(self):
        return self.elements[0]    

q1=Queue()
q1.enqueue(5)
q1.enqueue(7)

print(q1.elements)

q1.dequeue()
print(q1.elements)
q1.dequeue()
print(q1.elements)
q1.dequeue()