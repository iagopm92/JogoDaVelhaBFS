from jogodavelha import vazio, token, verificaGanhador


def movimentoIA(board, jogador): # função responsável pela verificação do melhor valor de jogada, do melhor movimento e as possibilidades de jogadas do algoritmo
    possibilidades = getPosicoes(board) # a variavel recebe as posições preenchidas no tabuleiro
    melhor_valor = None # melhor valor iniciada com valor nulo
    melhor_movimento = None # melhor movimento iniciada com valor nulo
    for possibilidade in possibilidades: # verificação de possibilidades de jogadas pelo algoritmo
        board[possibilidade[0]][possibilidade[1]] = token[jogador] 
        valor = algoritmoBusca(board, jogador) 
        board[possibilidade[0]][possibilidade[1]] = vazio
        if(melhor_valor is None): # atribuição do melhor valor de jogada a variavel valor
            melhor_valor = valor
            melhor_movimento = possibilidade
        elif(jogador == 0): # senao, é a vez do jogador 0
            if(valor > melhor_valor): 
                melhor_valor = valor
                melhor_movimento = possibilidade
        elif(jogador == 1):
            if(valor < melhor_valor):
                melhor_valor = valor
                melhor_movimento = possibilidade

    return melhor_movimento[0], melhor_movimento[1] # retorno do melhor movimento para o algoritmo


def getPosicoes(board):  # verifica as posiçõs do tabuleiro e adiciona elas em na fila posicoes
    posicoes = []
    for i in range(3):
        for j in range(3):
            if(board[i][j] == vazio):
                posicoes.append([i, j])
    
    return posicoes


score = {    # atribuição de um score a cada tipo de jogada
    "EMPATE": 0,
    "X": 1,
    "O": -1
}

# 
def algoritmoBusca(board, jogador): # função de busca de melhor valor para realização da jogada pelo algoritmo
    ganhador = verificaGanhador(board) 
    if(ganhador):
        return score[ganhador]
    jogador = (jogador + 1)%2
    
    possibilidades = getPosicoes(board)
    melhor_valor = None
    for possibilidade in possibilidades:
        board[possibilidade[0]][possibilidade[1]] = token[jogador]
        valor = algoritmoBusca(board, jogador)
        board[possibilidade[0]][possibilidade[1]] = vazio

        if(melhor_valor is None):
            melhor_valor = valor
        elif(jogador == 0):
            if(valor > melhor_valor):
                melhor_valor = valor
        elif(jogador == 1):
            if(valor < melhor_valor):
                melhor_valor = valor

    return melhor_valor
