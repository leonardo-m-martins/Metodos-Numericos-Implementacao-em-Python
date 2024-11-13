from copy import deepcopy

def triangulo_superior(matriz_: list):
    matriz = deepcopy(matriz_)
    for i in range(len(matriz)-1): # Verifica por quantas colunas iterar e o faz

        for idx,linha in enumerate(list(matriz)):  # Itera pelas linhas no sistema linear

            if idx - i <= 0: # Verifica se a linha atual não deve ser modificada (a linha 1 nunca é modificada!)
                continue

            m = linha[i] / matriz[i][i] # Encontra o multiplicador, linha[i] é equivalente a matriz[idx][i]

            # Obter a linha nova modificando termo por termo para manter o formato matriz
            for idx_termo in range(len(linha)):
                linha[idx_termo] = linha[idx_termo] - matriz[i][idx_termo] * m
            
            matriz[idx] = linha
            
    return matriz

def eliminacao_gauss(matriz: list):
    # TRIANGULO SUPERIOR
    matrizTriangulo = triangulo_superior(matriz)

    tamanho = len(matrizTriangulo[0])

    last_index = tamanho -1 # tamanho-1 porque a linha sempre tem um termo que não tem x
    Xs = [None for _ in range(last_index)] # LISTA PARA X1,X1,X3,...,Xn
    for idx,linha in reversed(list(enumerate(matrizTriangulo))): # Itera sobre as linhas reversamente

        for idx_termo,termo in reversed(list(enumerate(linha))): # Itera sobre os termos reversamente
            # Não faz nada se o termo for o mesmo do resultado (ex: termo 8 para 1*x1 + 4*x2 + 3*x3 = 8)
            if idx_termo == last_index:
                continue
            if Xs[idx_termo] != None:
                # Passa subtraindo para o resultado (ex: 1*x1 + 4*x2 = 8 - 3*x3)
                linha[last_index] -= termo * Xs[idx_termo]
            else:
                # Passa dividindo para descobrir o valor de Xn (ex: x2 = 8 / 4)
                # Pode gerar um erro se dividir por zero
                Xs[idx_termo] = linha[last_index] / termo
                break
        
    return Xs





def passos_triangulo_superior(matriz: list):
    matrizes = []
    for i in range(len(matriz)-1): # Verifica por quantas colunas iterar e o faz

        # ZERAR A1n, A2n,...
        for idx,linha in enumerate(list(matriz)):  # Itera pelas linhas no sistema linear

            if idx - i <= 0: # Verifica se a linha atual não deve ser modificada (a linha 1 nunca é modificada!)
                continue

            m = linha[i] / matriz[i][i] # Encontra o multiplicador, linha[i] é equivalente a matriz[idx][i]

            # Obter a linha nova modificando termo por termo para manter o formato matriz
            for idx_termo in range(len(linha)):
                linha[idx_termo] = linha[idx_termo] - matriz[i][idx_termo] * m
            
            matriz[idx] = linha
        matrizes.append(deepcopy(matriz))
        
    return matriz,matrizes

def passos_eliminacao_gauss(matriz: list):
    # TRIANGULO SUPERIOR
    matrizTriangulo,matrizes = passos_triangulo_superior(matriz)

    tamanho = len(matrizTriangulo[0])
    last_index = tamanho -1 # tamanho-1 porque a linha sempre tem um termo que não tem x
    Xs = [None for _ in range(last_index)] # LISTA PARA X1,X1,X3,...,Xn
    for linha in reversed(matrizTriangulo): # Itera sobre as linhas reversamente

        for idx_termo,termo in reversed(list(enumerate(linha))): # Itera sobre os termos reversamente
            # Não faz nada se o termo for o mesmo do resultado (ex: termo '8' para 1*x1 + 4*x2 + 3*x3 = 8)
            if idx_termo == last_index:
                continue

            if Xs[idx_termo] != None:
                # Passa subtraindo para o resultado (ex: 1*x1 + 4*x2 = 8 - 3*x3)
                linha[last_index] -= termo * Xs[idx_termo]
            
            else:
                # Passa dividindo para descobrir o valor de Xn (ex: x2 = 8 / 4)
                # Pode gerar um erro se dividir por zero
                Xs[idx_termo] = linha[last_index] / termo
                break
        
    return Xs,matrizes
        