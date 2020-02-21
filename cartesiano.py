"""Programa em Python que calcula a distância entre dois pontos, dadas as suas coordenadas. 
Considerando os pontos A(x1;y1) e B(x2;y2).

x1 é a abscissa de A, y1 é a ordenada de A.
x2 é a abscissa de B, y2 a ordenada de B
"""

# Importando biblioteca matemática para a função de raiz quadrada
from math import sqrt

def julian(x):

    if( x.isnumeric()):
        x = float(x)
        if(type(x) != float):
            return False
    
        else:
            return True
    else:
        return False

# Inserido coordenadas dos pontos
xA = input('Digite a abscissa do ponto A:')
while not julian(xA):
    print("Valor Invalidos")
    xA = input('Digite a abscissa do ponto A:')
xA = float(xA) 
 

xB = input('Digite a abscissa do ponto B:')
while not julian(xB):
    print("Valor Invalidos")
    xB = input('Digite a abscissa do ponto B:')
xB = float(xB)



yA = input('Digite a ordenada do ponto A:')
while not julian(yA):
    print("Valor Invalidos")
    yA = input('Digite a ordenada do ponto A:')
yA = float(yA)  

yB = input('Digite a abscissa do ponto B:')
while not julian(yB):
    print("Valor Invalidoss")
    yB = input('Digite a abscissa do ponto B:')
yB= float(yB)

# Calculando a distânciaa
distAB = sqrt(((xA-xB)**2) + ((yA-yB)**2))
print(distAB)


# Mostrando resultado
print('A distância entre esses dois pontos é de:', distAB, 'unidades de medida')