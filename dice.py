import random
def player():
    initial=random.randint(1,6)
    score=0
    for i in range(initial):
        b=random.randint(1,6)
        score+=b
    return score    
p1=player()
p2=player()
print(f'Player 1 score:{p1}')
print(f'Player 2 score:{p2}')
if p1>p2:
    print(f"Player 1 wins! and player 2  lost!")
elif p2>p1:
    print(f"Player 2 wins! and player 1 lost!")                
else:
    print(f"Tie!")