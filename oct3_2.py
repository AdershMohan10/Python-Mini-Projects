import random
#print(random.randint(1,10))
#fruits=['apple','orange','watmel','grps']
#print(random.choice(fruits))

#coin=['Heads','Tails']
#print(random.choice(coin))

#z=random.randint(1,2)
#if z==1:
#    print('heads')
#else:
#    print('tails')
import random
c=['Rock','Paper','Scissors']
c1=random.choice(c)
p=input('enter your choice \n 1.Rock\n 2.Paper\n 3.Scissors \nchoose...\n')
print(f'Computer Chose:{c1}')
    
if p=='Rock':
        if c1=='Rock':
            print('Tie')
        elif c1=='Paper':
            print('Computer Wins')
        elif c1=='Scissors':
            print('Player wins')        
elif p=='Paper':
        if c1=='Rock':
            print('Player wins')
        elif c1=='Paper':
            print('Tie')
        elif c1=='Scissors':
            print('Computer wins')
elif p=='Scissors':
        if c1=='Rock':
            print('Computer wins')
        elif c1=='Paper':
            print('Player Wins')
        elif c1=='Scissors':
            print('Tie')
    

