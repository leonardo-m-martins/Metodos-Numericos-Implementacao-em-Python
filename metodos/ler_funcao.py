from numpy import arcsin,arccos,arctan,sin,cos,tan,log,log10,sqrt,exp,e,pi,power,float_power,min,max,trunc,round,arccos,rad2deg,deg2rad,arcsinh,arccosh,arctanh,sinh,cosh,tanh
from math import factorial
from random import random
import re

'''
Entre com a função:
A expressão deve ser uma função da varíavel X. 
Funções suportadas: 
Seno de X: SIN(X)! 
Logaritmo neperiano de X: LN(X) 
Coseno de X: COS(X)! 
Logaritmo na base 10 de X: LOG10(X) Tangente de X: TAN(X)! 
Modulo de X: ABS(X)!
Logaritmo na base n de X: LOGN(n;X) 
Raiz Quadrada:SQRT(X)! 
Exponencial de X: EXP(X) 
Dicas: 
Raiz Cúbica de X: X^(1/3) 
Seno ao Quadrado de X: SIN(X)^2 
Seno de X ao Quadrado: SIN(X^2) 
Número Neperiano (E): EXP(1) 
Operadores: 
+ (soma); 
- (subtração); 
* (multiplicação); 
/ (divisão); 
^ (potenciação); 
MOD (resto da divisão inteira); 
DIV (quociente da divisão inteira); 
! (Fatorial); 
%(Porcentagem); 
Constante:E 
Constante:PI (3,14159)'''
class UserMathFunction():
    def __init__(self, string: str):
        self.string = string.lower()  # Normaliza para minúsculas
        self.elementos_permitidos = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                                     'x', '+', '-', '*', '/', '^', '!', '%', 'sin', 'cos',
                                     'arcsin', 'arctan', 'ln', 'abs', 'log10', 'log',
                                     'sqrt', 'exp', 'e', 'pi', ' ', '(', ')', 'power',
                                     'float_power', 'min', 'max', 'trunc', 'round', 
                                     'deg2rad', 'rad2deg', 'random','**','x',',','tan','factorial',
                                     'sinh','cosh','tanh','arcsinh','arccosh','arctanh','arccos')
        self.elements = self.parse()
        
        self.f = self.criar_funcao()
    
    def parse(self):
        # Regex para detectar números, variáveis, operadores e funções
        pattern = r"\b(?:arcsin|arctan|arccos|sin|cos|tan|arcsinh|arctanh|arccosh|sinh|cosh|tanh|ln|abs|log10|log|sqrt|exp|pi|e|x|power|float_power|min|max|trunc|factorial|round|deg2rad|\*\*|rad2deg|random)\b|[0-9]+(?:\.[0-9]+)?|[\+\-\*\/\^\!\%\(\)\,]"
        
        # Tokeniza a string usando a expressão regular
        tokens = re.findall(pattern, self.string)
        
        # Valida cada token para ver se ele está nos elementos permitidos
        for token in tokens:
            if token not in self.elementos_permitidos and not re.match(r"[0-9]+(?:\.[0-9]+)?", token):
                raise ValueError(f"Elemento '{token}' não é permitido.")
        
        # Verifica se a lista de tokens cobre toda a string original, sem nada extra
        reconstructed_string = ''.join(tokens)
        sanitized_string = re.sub(r"\s+", "", self.string)  # Remove espaços em branco
        
        if reconstructed_string != sanitized_string:
            raise ValueError(f"A expressão contém elementos não permitidos: {reconstructed_string} - {sanitized_string}.")
        
        return tokens
    
    def criar_funcao(self):
        def func(x):
            return eval(self.string)
        return func