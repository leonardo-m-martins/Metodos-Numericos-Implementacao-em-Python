def extrapolacao_parabola(tabela: dict,num_pontos: int,x_valor: float):
    Xs = list(tabela.keys())
    fXs = list(tabela.values())
    XfXs = [xn*fxn for xn,fxn in tabela.items()] # x * fx
    XsQuadrados = [xn**2 for xn in Xs]
    XsCubos = [xn**3 for xn in Xs]
    XsQuarta = [xn**4 for xn in Xs]
    

    # OBTER SOMAS
    soma_x = sum(Xs)
    soma_fx = sum(fXs)
    soma_xfx = sum(XfXs)
    soma_xQuadrado = sum(XsQuadrados)
    soma_xCubo = sum(XsCubos)
    soma_xQuarta = sum(XsQuarta)

    # MONTAR TABELA PARA EXIBIÇÃO NA INTERFACE
    tabelaNova = [
        Xs + [soma_x],
        fXs + [soma_fx],
        XfXs + [soma_xfx],
        XsQuadrados + [soma_xQuadrado],
        XsCubos + [soma_xCubo],
        XsQuarta + [soma_xQuarta]
    ]

    # CRIAR MATRIZ
    matriz = [
        [soma_xQuarta,soma_xCubo,soma_xQuadrado,soma_xfx],
        [soma_xCubo,soma_xQuadrado,soma_x,soma_xfx],
        [soma_xQuadrado,soma_x,num_pontos,soma_fx]
    ]

    # APLICAR ELIMINAÇÃO DE GAUSS
    from .metodo_eliminacao_gauss import eliminacao_gauss,triangulo_superior
    abc,trianguloSuperior = eliminacao_gauss(matriz),triangulo_superior(matriz)
    a = abc[0]
    b = abc[1]
    c = abc[2]

    # MONTAR FUNÇÃO f(x) = ax² + bx + c
    funcao = f'{a} * x**2 + {b} * x + {c}'
    def f(x):
        return eval(funcao)
    
    return f(x_valor),funcao,matriz,trianguloSuperior,tabelaNova