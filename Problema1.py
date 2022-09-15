import numpy as np
import math
#creamos una funcion para generar primos
def generar_primo():
    numero = 2
    yield numero
    while True:
        temp = numero
        while True:
            temp += 1
            contador = 1
            contador_divisores = 0
            while contador <= temp:
                if temp % contador == 0:
                    contador_divisores += 1
                if contador_divisores > 2:
                    break
                contador += 1
            if contador_divisores == 2:
                yield temp
                numero = temp
#fin de funcion          
m = 0
m = int(input('¿De que dimension quieres la matriz?'))
while m < 3:
  m = int(input('Dimesion menor a 3 ¿De que dimension quieres la matriz?'))
cprimos = m*m
g = generar_primo()
primos =[next(g)for _ in range(cprimos) ]
i = 0
j = 0
pos = 0
matriz = np.zeros((m,m))
for i in range(m):
    for j in range(m):
        matriz[i][j] = int(primos[pos])
        pos += 1
i = 0
j = 0
print('La matriz A de numeros primos consecutivos es:')
for i in range(m):
    for j in range (m):
        print(int(matriz[i][j]), end=" ")
    print()
i = 0
j = 0
sumasup = 0
j2=0
for i in range(m):
    for j in range (m):
        j2=j+i
        if j2 < m:
            sumasup=(int(matriz[i][j2]) + sumasup)
print('La suma de los elementos de la diagonal superior es:', sumasup)