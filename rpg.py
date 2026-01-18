import random
p=input("Enter player name:")
plhp=100
enhp=100
turn=1
while plhp>0 or enhp>0:
    print(f"Turn{turn}")
    print(f"{p} attacks enemy!")
    enhp=enhp-random.randint(1,20)
    print(f"enemy delt some damage remaining enemy hp:{enhp}")
    print(f"enemy attacks {p}!")
    plhp=plhp-random.randint(1,20)
    print(f"{p} delt some damage remaining {p} hp:{plhp}")
    if plhp<=0:
        print("Enemy wins")
        break
    elif enhp<=0:
        print(f"{p} wins")

    turn=turn+1    