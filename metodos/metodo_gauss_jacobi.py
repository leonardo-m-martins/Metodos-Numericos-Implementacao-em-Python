def gauss_jacobi(matriz: list,TOL,ordem: int,X0: list | None=None,MAX=10000):
    if X0 == None:
        X0 = [0 for _ in range(ordem)]
    Xs = [X0]

    for n in range(MAX):

        Xn = []

        # Itera sob a matriz
        for idx,linha in enumerate(matriz):
            resul = linha[ordem] # Iguala resul ao último elemento da matriz (se ordem=3, o quarto)
            # Itera sobre os Xses da última iteração, ou X0 se for a primeira iteração
            for i,x in enumerate(Xs[n]):
                # O idx indica qual X está sendo calculado, isolar esse X
                if i != idx: 
                    resul -= linha[i] * x
            # com o xn isolado, o resul é dividido pelo m em m*xn, gerando o valor de xn
            resul = resul / linha[idx]
            # adicionar o valor de xn à lista
            Xn.append(resul)
        # adicionar a lista à lista de listas
        Xs.append(Xn)

        # CRITÉRIO DE PARADA
        erroAbsoluto = max(abs(Xs[n][x] - Xn[x]) for x in range(ordem))
        if erroAbsoluto < TOL:
            return Xn,Xs,erroAbsoluto
    raise RuntimeError('Limite de iterações excedido')