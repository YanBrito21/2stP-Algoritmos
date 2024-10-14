import random
import time
lista=[]


for i in range (10000):
    n = random.randint(0,1000000)
    if n in lista:
        while n in lista:
            n = random.randint(0,1000000)
    lista.append(n)    
        
começo = time.perf_counter()

def bubbleSort(lista):
    n = len (lista)
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if lista[j] > lista[j + 1]:
                (lista[j], lista[j + 1]) = (lista[j + 1], lista[j])
    print(lista)

bubbleSort(lista)
final = time.perf_counter()
segundos = final - começo
print(f'Buble Sorte leva {segundos:.0f} segundos para ordenar uma lista de {len(lista)} números.')

começo = time.perf_counter()
def indiceMenor(lista, inicio):
    minimo = inicio
    n = len(lista)
    for j in range (inicio + 1, n):
        if lista[minimo] > lista[j]: 
            minimo = j
    return(minimo)
indiceMenor(lista, 0)

    
def selectionSort(lista):
    n = len (lista)
    for i in range(n - 1):
        minimo = indiceMenor(lista, i)
        (lista[i], lista[minimo]) = (lista[minimo], lista[i])
    print(lista)
selectionSort(lista)
final = time.perf_counter()
segundos = final - começo
print(f'Selection Sort leva {segundos:.0f} segundos para ordenar uma lista de {len(lista)} números.')
