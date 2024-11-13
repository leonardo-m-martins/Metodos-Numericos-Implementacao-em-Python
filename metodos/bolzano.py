def ap_bolzano(a,b,funcao,step=1,max=10000):
    n = int((b-a)//step)
    if n > max:
        return 'erro'
    if funcao(a) * funcao(b) < 0:
        valores = []
        valor = a
        for _ in range(n):
            valor += step
            imagem = funcao(valor)
            valores.append((valor,imagem))
        intervalos = []
        anterior = None
        for valor,imagem in valores:
            if anterior == None:
                anterior = [valor,imagem]
            else:
                if imagem * anterior[1] < 0:
                    intervalos.append([anterior[0],valor])
                anterior = [valor,imagem]
        if len(intervalos) == 0:
            return None
        return intervalos
    else:
        return None
    
def verificacao_bolzano(a,b,f):
    if f(a) * f(b) < 0:
        return True
    else:
        return False
    
# if __name__ == '__main__':
#     def func(x):
#         return x**3 - 6* (x**2) + 4 * x + 12
#     a = 1
#     b = 4
#     i = ap_bolzano(a,b,func,0.01)
#     print(i)
    