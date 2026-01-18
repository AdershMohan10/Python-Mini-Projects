def add(x,y):
    return x+y

def subt(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    if y==0:
        return 'Division by 0 not possible'
    else:
        return x/y
print('Welcome to Calculator! What do you wanna do?')

def main():
  while True:  
    n1=int(input('enter 1st num:'))
    n2=int(input('enter 2nd num:'))
    ch=input('enter your choice \n 1.Addition\n 2.Subtraction\n 3. Multiplication\n 4.Division\n 5.Exit\n choose...')

    if ch=='1':
        print(f'sum={add(n1,n2)}')
    elif ch=='2':
        print(f'diff={subt(n1,n2)}')
    elif ch=='3':
        print(f'product={mul(n1,n2)}')
    elif ch=='4':
        print(f'quotient={div(n1,n2)}')
    if ch=='5':
        print(f'sum={add(n1,n2)}')                

