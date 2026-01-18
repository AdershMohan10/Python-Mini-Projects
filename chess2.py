for i in range(1,9):
    for j in range(1,9):   
        if (i+j)%2==0:
            print('W ',end='')
        else:
            print('B ',end='')
    print()            