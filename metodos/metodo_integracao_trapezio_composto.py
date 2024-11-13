def trapezio_composto(f,n: int,x_inicial: float,x_final: float):
    h = (x_final - x_inicial)/n
    Xs = [x_inicial+h*i for i in range(1,n)]
    fXs = [f(xn) for xn in Xs]
    fx_i = f(x_inicial)
    resul_I = fx_i
    for fxn in fXs:
        resul_I += (fxn*2)
    fx_f = f(x_final)
    resul_I += fx_f
    print(resul_I)
    resul_I = resul_I * h /2

    # CRIAR TABELA PARA INTERFACE
    fXs.insert(0,fx_i)
    fXs.append(fx_f)
    Xs = [x_inicial] + Xs + [x_final]

    return resul_I,Xs,fXs,h

# if __name__ == '__main__':
#     from numpy import e
#     def f(x):
#         return e**x
#     print(trapezio_composto(f,4,0,1))