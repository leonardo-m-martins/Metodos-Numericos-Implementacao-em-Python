def interpolacao_lagrange(tabela: dict,x_valor: float,num_pontos: int):
    # CONSTRUIR O POLINÔMIO
    Xs = list(tabela.keys())
    fXs = list(tabela.values())
    Ls = []
    for i in range(num_pontos):
        l = ''
        for i2 in range(num_pontos):
            if i2 != i:
                li = f'(x - {Xs[i2]}) / ({Xs[i]} - {Xs[i2]})'
            else:
                continue
            if (i2<i and i2==0) or (i2>i and i2==1):
                l += f'( {li} )'
            else:
                l+=f'*( {li} )'
            
        Ls.append(l)
    Pn = ''
    for i in range(num_pontos):
        Pn += f'{Ls[i]} * {fXs[i]} + '
    Pn = Pn.removesuffix(' + ')


    # SIMPLIFICAR O POLINÔMIO
    from sympy import simplify,symbols
    x, y = symbols('x y')
    Pn_simplificada = simplify(Pn)

    # APLICAR PARA x
    def Polinomio(x):
        return eval(str(Pn_simplificada))
    
    return Polinomio(x=x_valor),Pn,Pn_simplificada

# if __name__ == '__main__':
#     tabela = {
#         2:3.1,
#         4:5.6
#     }
#     num_pontos = 2
#     x = 2.5
#     Pnx,Pn = interpolacao_lagrange(tabela,x,num_pontos)
#     print(Pnx,Pn)

#     tabela = {
#         8.1: 16.94410,
#         8.3: 17.56492,
#         8.6: 18.50515,
#         8.7: 18.82091
#     }
#     num_pontos = len(tabela)
#     x = 8.4
#     Pnx,Pn = interpolacao_lagrange(tabela,x,num_pontos)
#     print(Pn)

#     # import time
#     # tempo_entrada = time.time()
#     # from sympy import simplify,symbols

#     # x, y = symbols('x y')
#     # Pn_simplificada = simplify(Pn)

#     # print(Pn_simplificada)
#     # tempo_saida = time.time()
#     # print(tempo_saida-tempo_entrada)