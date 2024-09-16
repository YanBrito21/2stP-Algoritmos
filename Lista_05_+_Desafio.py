'''
# 1. Implemente uma função recursiva que calcule a potência de um número (base^expoente).
# 2. Crie uma função recursiva para calcular o n-ésimo termo da sequência de
Fibonacci.Lembre-se de que a sequência começa com 0 e 1.
# 3. Escreva uma função recursiva que conte quantos dígitos um número tem.
# 4. Escreva uma função recursiva que verifique se uma string é um palíndromo.
'''

# 1
def potencia(base , expoente):
    if expoente == 0:
        return 1
    return base * potencia(base,expoente-1)

result = potencia(3,3)
# print(result)


# 2
def fibonacci(f):
    if f == 0:
        return 0
    elif f == 1:
        return 1
    return fibonacci(f-1) + fibonacci(f-2)

result = fibonacci(10)
# print(result)


# 3 
def contagem(n):
    if n <10:
        return 1
    return 1 + contagem(n/10)

result = contagem(1000)
# print(result)

 
# 4
def palindromo(p):
    if len(p)==1 or len(p)==0:
        return 'É um palíndromo'
    elif p[0] != p[-1]:
        return 'Não é um palíndromo'
    return palindromo(p[1:-1])

result = palindromo('arara')
# print(result)


# Desafio
'''Escreva um algoritmo recursivo que crie uma senha gerada de forma aleatória e que seja criptografada caractere por caractere usando uma cifra de César simples.

Aqui está um exemplo com uma criptografia simples usando a técnica de cifra de César. Esse exemplo adiciona um deslocamento de 3 posições no valor ASCII de cada caractere da senha gerada.

Senha original: A1b2C3d4.               
Senha criptografada: D4e5F6g7'''
import random
import string
#lista = [] Lista para verificar se os numeros ou letras estão deslocando 3 posições no valor ASCII de cada caractere da senha gerada.
def senha(tamanho):
    caracteres = string.ascii_letters + string.digits
    if tamanho == 0:
        return ''
    caractere_aleatorio = random.choice(caracteres)
    #lista.append(caractere_aleatorio)           
    if caractere_aleatorio in caracteres:
        index = caracteres.index(caractere_aleatorio)
        caractere_criptografado = caracteres[(index+3) % len(caracteres)]
    return caractere_criptografado + senha(tamanho-1)

result = senha(8)
#print(lista)
print(result)

    
    

