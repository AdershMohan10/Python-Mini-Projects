board=[' ' for _ in range(9)]

def tt_board():
    print(board[0]+" | "+board[1]+" | "+board[2])
    print("--+---+--")
    print(board[3]+" | "+board[4]+" | "+board[5])
    print("--+---+--")
    print(board[6]+" | "+board[7]+" | "+board[8])

def winner(player):
    win=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for i in win:
        if board[i[0]]==board[i[1]]==board[i[2]]==player:
            return True
    return False

def play():
    current_player = "X"
    
    for _ in range(9):
        tt_board()
        choice=int(input(f"Player {current_player}, choose a position (1-9): ")) - 1
        
        if board[choice] != ' ':
            print("That space is already taken! Try again.")
            continue
        
        board[choice] = current_player
        
        if winner(current_player):
            tt_board()
            print(f"Player {current_player} wins!!!!")
            return
        
        current_player = "O" if current_player == "X" else "X"
    
    tt_board()
    print("It's a tie!")

play()


