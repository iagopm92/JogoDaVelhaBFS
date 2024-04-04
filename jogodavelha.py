vazio = " "
token = ["X", "O"]

def criarBoard():
    board = [
        [vazio, vazio, vazio],
        [vazio, vazio, vazio],
        [vazio, vazio, vazio],
    ]
    return board


def printBoard(board):
    for i in range (3):
        print("|".join(board[i]))
        if(i < 2):
            print("------")

def getInputValido(mensagem):
    try:
        n = int(input(mensagem))
        if(n >= 1 and n <= 3):
            return n - 1
        else:
            print("Número precisa estar entre 1 e 3")
            return getInputValido(mensagem)
    except:
        print("Número não valido!")
        return getInputValido(mensagem)

def verificaMovimento(board, i, j):
    if(board[i][j] == vazio):
        return True
    else:
        return False

def fazMovimento(board, i, j, jogador):
    board[i][j] = token[jogador]



def verificaGanhador(board):
    # verifica linhas
    for i in range(3):
        if(board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != vazio):
            return board[i][0]
   
   # verifica colunas
    for i in range(3):
        if(board[0][i] == board[1][i] and board[2][i] == board[0][i] and board[0][i] != vazio):
            return board[0][i]
    
    # diagonal principal   
    if(board[0][0] != vazio and board[0][0] == board[1][1] and board[1][1] == board[2][2]):    
            return board[0][0]
    
    # diagonal secundaria
    if(board[0][2] != vazio and board[0][2] == board[1][1] and board[1][1] == board[2][0]):    
            return board[0][2]
    
    for i in range(3):
        for j in range(3):
            if(board[i][j] == vazio):
                return False
    
    return "EMPATE"