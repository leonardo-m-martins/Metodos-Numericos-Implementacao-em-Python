# Recebe a função da integral f'(x) do usuário
def newton_raphson(x0,f,fi,TOL,MAX=10000):
    x = x0
    for _ in range(MAX):
        x_anterior = x
        x = x_anterior - (f(x)/fi(x))

        # CRITÉRIO DE PARADA
        if abs(x - x_anterior) < TOL or abs(f(x)) < TOL:
            return x
    raise RuntimeError('Limite de iterações excedido')

def passos_newton_raphson(x0,f,fi,TOL,MAX=10000):
    x = x0
    Xs = []
    for _ in range(MAX):
        Xs.append( (x,f(x),fi(x)) )
        x_anterior = x
        x = x_anterior - (f(x)/fi(x))

        # CRITÉRIO DE PARADA
        if abs(x - x_anterior) < TOL:
            return x,Xs,abs(x - x_anterior)
        elif abs(f(x)) < TOL:
            return x,Xs,abs(f(x))
    raise RuntimeError('Limite de iterações excedido')