def extrapolacao_reta(tabela: dict,num_pontos: int,x_valor: float):
    Xs = list(tabela.keys())
    fXs = list(tabela.values())
    XsQuadrados = [xn**2 for xn in Xs]
    XfXs = [xn*fxn for xn,fxn in tabela.items()] # x * fx

    # OBTER SOMAS
    soma_x = sum(Xs)
    soma_fx = sum(fXs)
    soma_xQuadrado = sum(XsQuadrados)
    soma_xfx = sum(XfXs)

    # MONTAR TABELA PARA EXIBIÇÃO NA INTERFACE
    tabelaNova = [
        Xs + [soma_x],
        fXs + [soma_fx],
        XsQuadrados + [soma_xQuadrado],
        XfXs + [soma_xfx]
    ]

    # CRIAR MATRIZ
    matriz = [
        [soma_xQuadrado,soma_x,soma_xfx],
        [soma_x,num_pontos,soma_fx]
    ]

    # APLICAR ELIMINAÇÃO DE GAUSS
    from .metodo_eliminacao_gauss import eliminacao_gauss,triangulo_superior
    ab,trianguloSuperior = eliminacao_gauss(matriz),triangulo_superior(matriz)
    a = ab[0]
    b = ab[1]

    # MONTAR FUNÇÃO f(x) = ax + b
    funcao = f'{a} * x + {b}'
    def f(x):
        return eval(funcao)
    
    return f(x_valor),funcao,matriz,trianguloSuperior,tabelaNova