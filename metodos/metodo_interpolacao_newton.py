def interpolacao_newton(tabela: dict,x: float,num_pontos: int):
    # TABELA DE DIFERENÇAS DIVIDIDAS
    tabelaDiferencasDivididas = [tabela]

    for idx in range(num_pontos-1):
        coluna = tabelaDiferencasDivididas[idx]
        proximaColuna = []
        if type(coluna) == dict:
            Xs = list(coluna.keys())
            fXs = list(coluna.values())

            for i in range(num_pontos-1):
                diferencaDividida = ( fXs[i+1] - fXs[i] ) / ( Xs[i+1] - Xs[i])
                proximaColuna.append(diferencaDividida)
        else:
            for i in range(len(coluna)-1):
                diferencaDividida = ( coluna[i+1] - coluna[i] ) / ( Xs[i+1+idx] - Xs[i] )
                proximaColuna.append(diferencaDividida)

        tabelaDiferencasDivididas.append(proximaColuna)
    
    # POLINÔMIO DE LAGRANGE
    for idx,coluna in enumerate(tabelaDiferencasDivididas):
        if idx==0:
            Pdex = f'{fXs[0]}'
            continue
        Pdex += ' + '
        for i in range(idx):
            if i != 0:
                Pdex += ' * '
            Pdex += f'(x - {Xs[i]})'
        Pdex += f' * {coluna[0]}'
    
    def Pn(x):
        return eval(Pdex)
    
    return Pn(x),Pdex,tabelaDiferencasDivididas

    