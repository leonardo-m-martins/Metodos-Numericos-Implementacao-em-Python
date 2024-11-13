def gauss_seidel(matriz: list,TOL,ordem: int,X0: list | None=None,MAX=10000):
    if X0 == None:
        X0 = [0 for _ in range(ordem)]
    Xs = [X0]

    for n in range(MAX):
        Xseidel = Xs[n].copy()
        Xn = []
        for idx,linha in enumerate(matriz):
            
            resul = linha[ordem]
            for i,x in enumerate(list(Xseidel)):
                if i != idx:
                    resul -= linha[i] * x
            resul = resul / linha[idx]
            Xseidel[idx] = resul # Aplica o novo valor de Xn para os próximos cálculos na iteração
            Xn.append(resul)
        Xs.append(Xn)

        # CRITÉRIO DE PARADA
        erroAbsoluto = max(abs(Xs[n][x] - Xn[x]) for x in range(ordem))
        if erroAbsoluto < TOL:
            return Xn,Xs,erroAbsoluto


    raise RuntimeError('Limite de iterações excedido')