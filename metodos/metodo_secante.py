def secante(x0,x1,f,TOL,MAX=10000):
    for _ in range(MAX):
        # CRITÉRIO DE PARADA
        if abs(x1 - x0) < TOL or abs(f(x1)) < TOL:
            return x1
        
        x0, x1 = x1, ( x0 * f(x1) - x1 * f(x0) ) / ( f(x1) - f(x0) )
    
    raise RuntimeError('Limite de iterações excedido')

def passos_secante(x0,x1,f,TOL,MAX=10000):
    Xs = [(x0,f(x0))]
    for _ in range(MAX):
        fx0 = f(x0)
        fx1 = f(x1)
        Xs.append( (x1,fx1) )

        # CRITÉRIO DE PARADA
        if abs(x1 - x0) < TOL:
            return x1,Xs,abs(x1 - x0)
        elif abs(fx1) < TOL:
            return x1,Xs,abs(fx1)
        
        # SECANTE (x1 é xn)
        x0, x1 = x1, ( x0 * fx1 - x1 * fx0 ) / ( fx1 - fx0 )
    
    raise RuntimeError('Limite de iterações excedido')