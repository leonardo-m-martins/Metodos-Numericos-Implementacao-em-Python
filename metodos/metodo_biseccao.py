from .bolzano import verificacao_bolzano

def bisseccao(intervalo,TOL,f,MAX=10000):
    if not verificacao_bolzano(intervalo[0],intervalo[1],f):
        raise NameError('Intervalo inválido')
    no_tol = True
    a = intervalo[0]
    b = intervalo[1]
    for _ in range(MAX):
        # BISSECÇÃO
        m = (a+b)/2
        if verificacao_bolzano(a,m,f):
            b = m
        else:
            a = m
        
        # CRITÉRIO DE PARADA
        if f(m) == 0 or abs(b-a) < TOL or abs(f(m)) < TOL:
            return m
    
    raise RuntimeError('Limite de iterções excedido')

def passos_bisseccao(intervalo,TOL,f,MAX=10000):
    if not verificacao_bolzano(intervalo[0],intervalo[1],f):
        raise ValueError('Intervalo inválido')
    no_tol = True
    a = intervalo[0]
    b = intervalo[1]
    bisseccoes = []
    for _ in range(MAX):
        # BISSECÇÃO
        m = (a+b)/2
        fa_sinal = '-' if f(a) < 0 else '+'
        fm_sinal = '-' if f(m) < 0 else '+'
        fb_sinal = '-' if f(b) < 0 else '+'
        bisseccoes.append( ( a,fa_sinal,m,fm_sinal,b,fb_sinal ) )
        if verificacao_bolzano(a,m,f):
            b = m
        else:
            a = m
        
        # CRITÉRIO DE PARADA
        if f(m) == 0:
            return m,bisseccoes,0
        elif abs(b-a) < TOL:
            return m,bisseccoes,abs(b-a)
        elif abs(f(m)) < TOL:
            return m,bisseccoes,abs(f(m))
    
    raise RuntimeError('Limite de iterções excedido')
    