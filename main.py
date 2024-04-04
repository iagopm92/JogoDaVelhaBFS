
# Jogo da velha desenvolvido em python de uma jogador contra um algoritmo de verificação de possibilidades de melhor caminho


from jogodavelha import criarBoard, fazMovimento, getInputValido, \
                            printBoard, verificaGanhador, verificaMovimento
from algoritmoBusca import movimentoIA

jogador = 0 # o jogador recebe o valor de 0
board = criarBoard() # chama a função de criação do tabuleiro do jogo
ganhador = verificaGanhador(board) # variavel que recebe o resultado da função de verificação do ganhador do jogo
while(not ganhador): # enquanto o ganhador não for achado executa as os comandos abaixo
    printBoard(board) # printa na tela o tabuleiro preenchido após cada jogada
    print("=================")
    if(jogador == 0): # verifica se a vez é do algoritmo ou do jogador 0
        i,j = movimentoIA(board, jogador) #recebe a jogada do algoritmo
    else:
        i = getInputValido("Digite a linha: ")  # jogador insere a linha a ser inserido a "O"                                
        j = getInputValido("Digite a coluna: ") # jogador insere a coluna a ser inserido a "O"

    if(verificaMovimento(board, i, j)): # chama a função de verificação do movimento 
        fazMovimento(board, i, j, jogador) # chama a função de jogada do algoritmo
        jogador = (jogador + 1)%2 # analisa se é a vez do jogador 0 ou do algoritmo de jogar
    else: 
        print("A posição informada já está ocupada") # essa tela aparece caso o valor campo escolhido pelo jogador já tiver sido preenchido anteriormente

    ganhador = verificaGanhador(board) # recebe o retorno da função de verificação do ganhador
print("=================")
printBoard(board) # imprime o tabuleiro final
print("O resultado é: ", ganhador) # imprime o ganhador 
print("=================")