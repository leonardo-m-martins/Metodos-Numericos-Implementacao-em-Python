from flask import Flask, render_template, request
from metodos import (ler_funcao,bolzano,metodo_biseccao,
                     metodo_extrapolacao_parabola,metodo_extrapolacao_reta,metodo_gauss_jacobi,
                     metodo_gauss_seidel,metodo_integracao_trapezio_composto,
                     metodo_interpolacao_newton,metodo_interpolacao_lagrange,metodo_newton_raphson,
                     metodo_secante,metodo_eliminacao_gauss)
import webbrowser
import threading
import time
import argparse

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bolzano',methods=['GET','POST'])
def app_bolzano():
    template = 'bolzano.html'
    if request.method == 'POST':
        # PEGAR PARÂMETROS
        try:
            funcao = str(request.form['funcao'])
            funcao = ler_funcao.UserMathFunction(funcao)
        except Exception as e:
            avaliacaoFuncao = f'Erro: {e}'
            return render_template(template,limite_inferior=None,avaliacaoFuncao=avaliacaoFuncao)
        
        try:
            limite_inferior = float(request.form['limite_inferior'])
        except Exception as e:
            avaliarFloat = f'Erro: {e}'
            return render_template(template,limite_inferior=None,avaliarFloat=avaliarFloat)
        
        try:
            limite_superior = float(request.form['limite_superior'])
        except Exception as e:
            avaliarFloat = f'Erro: {e}'
            return render_template(template,limite_inferior=None,avaliarFloat=avaliarFloat)
        
        step = request.form['step'] if request.form['step'] else '1'
        try:
            step = float(step)
        except Exception as e:
            avaliarFloat = f'Erro: {e}'
            return render_template(template,limite_inferior=None,avaliarFloat=avaliarFloat)
        
        intervalo = bolzano.ap_bolzano(limite_inferior,limite_superior,funcao.f,step)

        return render_template(template,intervalo=intervalo,
                               limite_inferior=limite_inferior,limite_superior=limite_superior,
                               step=step)
    
    return render_template(template,limite_inferior=None)

@app.route('/bisseccao', methods=['GET', 'POST'])
def app_bisseccao():
    template = 'bisseccao.html'
    if request.method == 'POST':
        #########################
        # PEGAR PARÂMETROS
        #########################

        # Função (matemática)
        try:
            funcao = str(request.form['funcao'])
            funcao = ler_funcao.UserMathFunction(funcao)
            f = funcao.f
        except Exception as e:
            avaliacaoFuncao = f'Erro: {e}'
            return render_template(template,limite_inferior=None,avaliacaoFuncao=avaliacaoFuncao)
        # Limite inferior do intervalo
        try:
            limite_inferior = float(request.form['limite_inferior'])
        except Exception as e:
            avaliarFloatLimInferior = f'Erro: {e}'
            return render_template(template,limite_inferior=None,avaliarFloatLimInferior=avaliarFloatLimInferior)
        # Limite superior do intervalo
        try:
            limite_superior = float(request.form['limite_superior'])
        except Exception as e:
            avaliarFloatLimSuperior = f'Erro: {e}'
            return render_template(template,limite_inferior=None,avaliarFloatLimSuperior=avaliarFloatLimSuperior)
        # Tolerância (tol)
        try:
            tol = request.form['TOL'] if request.form['TOL'] else '0.0001'
            tol = float(tol)
        except Exception as e:
            avaliarFloatTOL = f'Erro: {e}'
            return render_template(template,limite_inferior=None,avaliarFloatTOL=avaliarFloatTOL)
        
        ##############################
        # APLICAR MÉTODO
        ##############################

        x,bisseccoes,erroAbsoluto = metodo_biseccao.passos_bisseccao([limite_inferior,limite_superior],tol,f)

        # Exibir os parâmetros recebidos na página de resposta
        return render_template(template, 
                               limite_inferior=limite_inferior, 
                               limite_superior=limite_superior, 
                               TOL=tol,x=x,bisseccoes=bisseccoes,erroAbsoluto=erroAbsoluto)
    
    return render_template(template,limite_inferior=None)

@app.route('/newton_raphson', methods=['GET', 'POST'])
def app_newton_raphson():
    template = 'newton_raphson.html'
    if request.method == 'POST':
        #########################
        # PEGAR PARÂMETROS
        #########################

        # Função (matemática)
        try:
            funcao = str(request.form['funcao'])
            funcao = ler_funcao.UserMathFunction(funcao)
            f = funcao.f
        except Exception as e:
            avaliacaoFuncao = f'Erro: {e}'
            return render_template(template,x=None,avaliacaoFuncao=avaliacaoFuncao)
        # Derivada
        funcaoDerivada = str(request.form['funcaoDerivada'])
        try:
            funcaoDerivada = ler_funcao.UserMathFunction(funcaoDerivada)
            fi = funcaoDerivada.f
        except Exception as e:
            avaliacaoFuncao = f'Erro: {e}'
            return render_template(template,x=None,avaliacaoFuncao=avaliacaoFuncao)
        # x0
        try:
            x0 = float(request.form['x0'])
        except Exception as e:
            avaliarFloatX0 = f'Erro: {e}'
            return render_template(template,x=None,avaliarFloatX0=avaliarFloatX0)
        # Tolerância (tol)
        try:
            tol = request.form['TOL'] if request.form['TOL'] else '0.0001'
            tol = float(tol)
        except Exception as e:
            avaliarFloatTOL = f'Erro: {e}'
            return render_template(template,x=None,avaliarFloatTOL=avaliarFloatTOL)
        
        ##############################
        # APLICAR MÉTODO
        ##############################
        try:
            x,Xs,erroAbsoluto = metodo_newton_raphson.passos_newton_raphson(x0,f,fi,tol)
        except Exception as e:
            erroMetodo = f'Erro: {e}'
            return render_template(template,x=None, erroMetodo=erroMetodo)

        # Exibir os parâmetros recebidos na página de resposta
        return render_template(template,Xs=Xs,TOL=tol,x=x,erroAbsoluto=erroAbsoluto)
    
    return render_template(template,x=None)

@app.route('/secante', methods=['GET', 'POST'])
def app_secante():
    template = 'secante.html'
    if request.method == 'POST':
        #########################
        # PEGAR PARÂMETROS
        #########################

        # Função (matemática)
        funcao = str(request.form['funcao'])
        try:
            funcao = ler_funcao.UserMathFunction(funcao)
            f = funcao.f
        except Exception as e:
            avaliacaoFuncao = f'Erro: {e}'
            return render_template(template,x=None,avaliacaoFuncao=avaliacaoFuncao)
        # x0
        try:
            x0 = float(request.form['x0'])
        except Exception as e:
            avaliarFloatX0 = f'Erro: {e}'
            return render_template(template,x=None,avaliarFloatX0=avaliarFloatX0)
        # x1
        try:
            x1 = float(request.form['x1'])
        except Exception as e:
            avaliarFloatX1 = f'Erro: {e}'
            return render_template(template,x=None,avaliarFloatX1=avaliarFloatX1)
        # Tolerância (tol)
        try:
            tol = request.form['TOL'] if request.form['TOL'] else '0.0001'
            tol = float(tol)
        except Exception as e:
            avaliarFloatTOL = f'Erro: {e}'
            return render_template(template,x=None,avaliarFloatTOL=avaliarFloatTOL)
        
        ##############################
        # APLICAR MÉTODO
        ##############################
        try:
            x,Xs,erroAbsoluto = metodo_secante.passos_secante(x0,x1,f,tol)
        except Exception as e:
            erroMetodo = f'Erro: {e}'
            return render_template(template,x=None, erroMetodo=erroMetodo)

        # Exibir os parâmetros recebidos na página de resposta
        return render_template(template,Xs=Xs,TOL=tol,x=x,erroAbsoluto=erroAbsoluto)
    
    return render_template(template,x=None)

@app.route('/eliminacao_gauss', methods=['GET', 'POST'])
def app_eliminacao_gauss():
    template = 'eliminacao_gauss.html'
    if request.method == 'POST':
        #########################
        # PEGAR PARÂMETROS
        #########################
        # Ordem
        ordem = int(request.form['ordem'])
        tabela = {}
        # Matriz/sistema linear
        for key in request.form:
            if key.startswith('tabelaEG-'):
                _,i,j = key.split('-')
                i,j = int(i), int(j)
                try:
                    tabela[(i,j)] = float(request.form[key])
                except Exception as e:
                    erroValores = f'Erro: {e}'
                    return render_template(template,Xs=None,erroValores=erroValores)
        
        matriz = [
            [tabela[(i,j)] for j in range(ordem+1)] for i in range(ordem)
        ]

        # Aplicar o método
        try:
            Xs,matrizes = metodo_eliminacao_gauss.passos_eliminacao_gauss(matriz)
        except Exception as e:
            erroMetodo = f'Erro (método): {e}'
            return render_template(template,Xs=None,erroMetodo=erroMetodo)

        return render_template(template,Xs=Xs,matrizes=matrizes)
    
    return render_template(template,Xs=None)

@app.route('/gauss_jacobi', methods=['GET', 'POST'])
def app_gauss_jacobi():
    template = 'gauss_jacobi.html'
    if request.method == 'POST':
        #########################
        # PEGAR PARÂMETROS
        #########################
        # ordem
        ordem = int(request.form['ordem'])
        tabela = {}
        x0 = [0.0 for _ in range(ordem)]
        # Tolerância
        try:
            tol = request.form['TOL'] if request.form['TOL'] else '0.0001'
            tol = float(tol)
        except Exception as e:
            avaliarFloatTOL = f'Erro: {e}'
            return render_template(template,Xs=None,avaliarFloatTOL=avaliarFloatTOL)

        # Ler tabela e X0
        try:
            for key in request.form:
                if key.startswith('tabelaGJ-') and not key.startswith('tabela-x'):
                    _,i,j = key.split('-')
                    i,j = int(i), int(j)
                    tabela[(i,j)] = float(request.form[key])
                elif key.startswith('tabelaGJ-x'):
                    if request.form[key]:
                        _,_,k = key.split('-')
                        x0[k] = float(request.form[key])
        except Exception as e:
            erroValores = f'Erro: {e}'
            return render_template(template,Xs=None,erroValores=erroValores)
        # Criar matriz
        matriz = [
            [tabela[(i,j)] for j in range(ordem+1)] for i in range(ordem)
        ]

        # Aplicar método gauss jacobi
        try:
            Xs,matrizes,erroAbsoluto = metodo_gauss_jacobi.gauss_jacobi(matriz,tol,ordem,x0)
        except Exception as e:
            erroMetodo = f'Erro (método): {e}'
            return render_template(template,Xs=None,erroMetodo=erroMetodo)

        return render_template(template,Xs=Xs,matrizes=matrizes,erroAbsoluto=erroAbsoluto)
    
    return render_template(template,Xs=None)

@app.route('/gauss_seidel', methods=['GET', 'POST'])
def app_gauss_seidel():
    template = 'gauss_seidel.html'
    if request.method == 'POST':
        #########################
        # PEGAR PARÂMETROS
        #########################
        # ordem
        ordem = int(request.form['ordem'])
        tabela = {}
        x0 = [0.0 for _ in range(ordem)]
        # Tolerância
        try:
            tol = request.form['TOL'] if request.form['TOL'] else '0.0001'
            tol = float(tol)
        except Exception as e:
            avaliarFloatTOL = f'Erro: {e}'
            return render_template(template,Xs=None,avaliarFloatTOL=avaliarFloatTOL)

        # Ler tabela e X0
        try:
            for key in request.form:
                if key.startswith('tabelaGS-') and not key.startswith('tabela-x'):
                    _,i,j = key.split('-')
                    i,j = int(i), int(j)
                    tabela[(i,j)] = float(request.form[key])
                elif key.startswith('tabelaGS-x'):
                    if request.form[key]:
                        _,_,k = key.split('-')
                        x0[k] = float(request.form[key])
        except Exception as e:
            erroValores = f'Erro: {e}'
            return render_template(template,Xs=None,erroValores=erroValores)
        # Criar matriz
        matriz = [
            [tabela[(i,j)] for j in range(ordem+1)] for i in range(ordem)
        ]

        # Aplicar método gauss seidel
        try:
            Xs,matrizes,erroAbsoluto = metodo_gauss_seidel.gauss_seidel(matriz,tol,ordem,x0)
        except Exception as e:
            erroMetodo = f'Erro (método): {e}'
            return render_template(template,Xs=None,erroMetodo=erroMetodo)

        return render_template(template,Xs=Xs,matrizes=matrizes,erroAbsoluto=erroAbsoluto)
    
    return render_template(template,Xs=None)

@app.route('/interpolacao_newton', methods=['GET', 'POST'])
def app_interpolacao_newton():
    template = 'interpolacao_newton.html'
    if request.method == 'POST':
        #########################
        # PEGAR PARÂMETROS
        #########################
        # pontos
        pontos = int(request.form['pontos'])
        tabela = {}
        
        # Ler tipo
        tipo = str(request.form['tipo'])
        if tipo == 'Normal':
            # Interpolação normal
            tabelaX = 'tabelaIN-x'
            tabelafX = 'tabelaIN-fx'
        else:
            # Interpolação inversa
            tabelaX = 'tabelaIN-fx'
            tabelafX = 'tabelaIN-x'
        # Ler X/f(X)
        try:
            x = float(request.form['x'])
        except Exception as e:
            avaliarFloatX = f'Erro: {e}'
            return render_template(template,resul_x=None,avaliarFloatX=avaliarFloatX)

        dict_auxiliar = {}


        # Ler tabela de pontos
        try:
            for key in request.form:
                if key.startswith(tabelaX):
                    _,_,i = key.split('-')
                    dict_auxiliar[i] = float(request.form[key])
            for key in request.form:
                if key.startswith(tabelafX):
                    if request.form[key]:
                        _,_,j = key.split('-')
                        tabela[dict_auxiliar[j]] = float(request.form[key])
        except Exception as e:
            erroValores = f'Erro: {e}'
            return render_template(template,resul_x=None,erroValores=erroValores)

        # Aplicar método Interpolação Newton
        try:
            resul_x,Pn,tabelaDiferencasDivididas = metodo_interpolacao_newton.interpolacao_newton(tabela=tabela,x=x,num_pontos=pontos)
        except Exception as e:
            erroMetodo = f'Erro (método): {e}'
            return render_template(template,resul_x=None,erroMetodo=erroMetodo)

        return render_template(template,resul_x=resul_x,Pn=Pn,tabelaDiferencasDivididas=tabelaDiferencasDivididas,tipo=tipo,x=x)
    
    return render_template(template,resul_x=None)

@app.route('/interpolacao_lagrange', methods=['GET', 'POST'])
def app_interpolacao_lagrange():
    template = 'interpolacao_lagrange.html'
    if request.method == 'POST':
        #########################
        # PEGAR PARÂMETROS
        #########################
        # pontos
        pontos = int(request.form['pontos'])
        tabela = {}
        
        # Ler tipo
        tipo = str(request.form['tipo'])
        if tipo == 'Normal':
            # Interpolação normal
            tabelaX = 'tabelaIL-x'
            tabelafX = 'tabelaIL-fx'
        else:
            # Interpolação inversa
            tabelaX = 'tabelaIL-fx'
            tabelafX = 'tabelaIL-x'
        # Ler X/f(X)
        try:
            x = float(request.form['x'])
        except Exception as e:
            avaliarFloatX = f'Erro: {e}'
            return render_template(template,resul_x=None,avaliarFloatX=avaliarFloatX)

        dict_auxiliar = {}


        # Ler tabela de pontos
        try:
            for key in request.form:
                if key.startswith(tabelaX):
                    _,_,i = key.split('-')
                    dict_auxiliar[i] = float(request.form[key])
            for key in request.form:
                if key.startswith(tabelafX):
                    if request.form[key]:
                        _,_,j = key.split('-')
                        tabela[dict_auxiliar[j]] = float(request.form[key])
        except Exception as e:
            erroValores = f'Erro: {e}'
            return render_template(template,resul_x=None,erroValores=erroValores)

        # Aplicar método Interpolação Lagrange
        try:
            resul_x,Pn,Pn_simplificado = metodo_interpolacao_lagrange.interpolacao_lagrange(tabela=tabela,x_valor=x,num_pontos=pontos)
        except Exception as e:
            erroMetodo = f'Erro (método): {e}'
            return render_template(template,resul_x=None,erroMetodo=erroMetodo)

        return render_template(template,resul_x=resul_x,Pn=Pn,Pn_simplificado=str(Pn_simplificado),tipo=tipo,x_valor=x)
    
    return render_template(template,resul_x=None)

@app.route('/extrapolacao_reta', methods=['GET', 'POST'])
def app_extrapolacao_reta():
    template = 'extrapolacao_reta.html'
    if request.method == 'POST':
        #########################
        # PEGAR PARÂMETROS
        #########################
        # pontos
        pontos = int(request.form['pontos'])
        tabela = {}
        
        tabelaX = 'tabelaExtrR-x'
        tabelafX = 'tabelaExtrR-fx'
        # Ler X/f(X)
        try:
            x = float(request.form['x'])
        except Exception as e:
            avaliarFloatX = f'Erro: {e}'
            return render_template(template,resul_x=None,avaliarFloatX=avaliarFloatX)

        dict_auxiliar = {}


        # Ler tabela de pontos
        try:
            for key in request.form:
                if key.startswith(tabelaX):
                    _,_,i = key.split('-')
                    dict_auxiliar[i] = float(request.form[key])
            for key in request.form:
                if key.startswith(tabelafX):
                    if request.form[key]:
                        _,_,j = key.split('-')
                        tabela[dict_auxiliar[j]] = float(request.form[key])
        except Exception as e:
            erroValores = f'Erro: {e}'
            return render_template(template,resul_x=None,erroValores=erroValores)

        # Aplicar método Extrpolação Reta
        try:
            resul_x,funcao,matriz,trianguloSuperior,tabelaNova = metodo_extrapolacao_reta.extrapolacao_reta(tabela=tabela,num_pontos=pontos,x_valor=x)
        except Exception as e:
            erroMetodo = f'Erro (método): {e}'
            return render_template(template,resul_x=None,erroMetodo=erroMetodo)
        
        nomes = ['','x','f(x)','x**2','x*f(x)']

        return render_template(template,resul_x=resul_x,funcao=funcao,
                               matriz=matriz,trianguloSuperior=trianguloSuperior,
                               tabelaNova=tabelaNova,x_valor=x,nomes=nomes, num_pontos=pontos)
    
    return render_template(template,resul_x=None)

@app.route('/extrapolacao_parabola', methods=['GET', 'POST'])
def app_extrapolacao_parabola():
    template = 'extrapolacao_parabola.html'
    if request.method == 'POST':
        #########################
        # PEGAR PARÂMETROS
        #########################
        # pontos
        pontos = int(request.form['pontos'])
        tabela = {}
        
        tabelaX = 'tabelaExtr-x'
        tabelafX = 'tabelaExtr-fx'
        # Ler X/f(X)
        try:
            x = float(request.form['x'])
        except Exception as e:
            avaliarFloatX = f'Erro: {e}'
            return render_template(template,resul_x=None,avaliarFloatX=avaliarFloatX)

        dict_auxiliar = {}


        # Ler tabela de pontos
        try:
            for key in request.form:
                if key.startswith(tabelaX):
                    _,_,i = key.split('-')
                    dict_auxiliar[i] = float(request.form[key])
            for key in request.form:
                if key.startswith(tabelafX):
                    if request.form[key]:
                        _,_,j = key.split('-')
                        tabela[dict_auxiliar[j]] = float(request.form[key])
        except Exception as e:
            erroValores = f'Erro: {e}'
            return render_template(template,resul_x=None,erroValores=erroValores)

        # Aplicar método Extrapolação Parábola
        try:
            resul_x,funcao,matriz,trianguloSuperior,tabelaNova = metodo_extrapolacao_parabola.extrapolacao_parabola(tabela=tabela,num_pontos=pontos,x_valor=x)
        except Exception as e:
            erroMetodo = f'Erro (método): {e}'
            return render_template(template,resul_x=None,erroMetodo=erroMetodo)
        
        nomes = ['','x','f(x)','x*f(x)','x**2','x**3','x**4']

        return render_template(template,resul_x=resul_x,funcao=funcao,
                               matriz=matriz,trianguloSuperior=trianguloSuperior,
                               tabelaNova=tabelaNova,x_valor=x,nomes=nomes,num_pontos=pontos)
    
    return render_template(template,resul_x=None)

@app.route('/integracao_trapezio_composto',methods=['GET','POST'])
def app_integracao_trapezio_composto():
    template = 'integracao_trapezio_composto.html'
    if request.method == 'POST':
        # PEGAR PARÂMETROS
        try:
            funcao = str(request.form['funcao'])
            funcao = ler_funcao.UserMathFunction(funcao)
            f = funcao.f
        except Exception as e:
            avaliacaoFuncao = f'Erro: {e}'
            return render_template(template,integral=None,avaliacaoFuncao=avaliacaoFuncao)
        
        try:
            x_inicial = float(request.form['limite_inferior'])
        except Exception as e:
            avaliarFloat = f'Erro: {e}'
            return render_template(template,integral=None,avaliarFloat=avaliarFloat)
        
        try:
            x_final = float(request.form['limite_superior'])
        except Exception as e:
            avaliarFloat = f'Erro: {e}'
            return render_template(template,integral=None,avaliarFloat=avaliarFloat)
        
        try:
            num_pontos = int(request.form['pontos'])
        except Exception as e:
            avaliarInt = f'Erro: {e}'
            return render_template(template,integral=None,avaliarInt=avaliarInt)
        
        integral,Xs,fXs,h = metodo_integracao_trapezio_composto.trapezio_composto(f,num_pontos-1,x_inicial,x_final)

        return render_template(template,integral=integral,Xs=Xs,fXs=fXs,num_pontos=num_pontos,h=h)
    
    return render_template(template,integral=None)
    
def open_browser():
    time.sleep(3)  # Aguarda três segundos para que o servidor já esteja rodando
    webbrowser.open("http://127.0.0.1:5000")

if __name__ == "__main__":
    print("Iniciando o servidor Flask. Por favor, aguarde...")
    # print("O navegador será aberto automaticamente assim que o servidor estiver pronto.")
    # threading.Thread(target=open_browser).start()  # Abre o navegador em uma nova thread

    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='127.0.0.1', help='Host do servidor')
    parser.add_argument('--port', type=int, default=5000, help='Porta do servidor')
    args = parser.parse_args()

    app.run(host=args.host, port=args.port)
