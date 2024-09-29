# Exercicio 1
import random

lista = []

for i in range(1,10+1):
    i = (random.randint(0,99))
    lista.append(i)
print(lista)

def MinMaxLista(l):
    return(f'Menor numero da lista: {min(l)}\nMaior numero da lista: {max(l)}')
    
result = MinMaxLista(lista)
print(result)

# exercicio 2  

frutas = []
def adicionar_frutas():
    for fruta in range(1,5+1):
        fruta = input('Digite o nome da fruta: ')
        frutas.append(fruta)
        
def lista_frutas():
    fruta = input('Digite qual fruta deseja buscar: ')
    if fruta in frutas:
        print(f'{fruta} esta na lista!')
    else:
        print(f'{fruta} não esta na lista!')
     
while True:
    menu = input('digite [1] para adicionar frutas, [2] para verificar frutas ou [3] para sair: ')
    if menu == '1':
        adicionar_frutas()
    elif menu == '2':
        lista_frutas()
    elif menu == '3':
        break
    else:
        print('Essa opção não existe')
        
# Exercicio 3
import random
numeros = []

for i in range(1,10+1):
    i = random.randint(0,99)
    numeros.append(i)
print(numeros)

def media(lista):
    return sum(lista)/len(lista)
    
result = media(numeros)
print(result)

# Exercicio 4

def aninhada(nome, idade, cidade):
    pessoas = [['jose', 23,'saquarema'], ['yan', 23, 'saquarema']]
    pessoa = list((nome,idade,cidade))
    pessoas.append(pessoa)
    for pessoa in pessoas:
        print(f'Nome: {pessoa[0]}, idade: {pessoa[1]}, cidade: {pessoa[2]}')

aninhada('josé', 23, 'Saquarema')

# Exercicio 5

numeros = [23, 56 , 56, 78, 23, 89, 90, 45, 34, 45, 34, 70]
dicionario = dict.fromkeys(numeros, 'ok')
result = dicionario.keys()
for i in result:
    print(i, end=' ')

lista_numeros = []
for numero in numeros:
    if numero not in lista_numeros:
        lista_numeros.append(numero)
print(lista_numeros)

# Exercicio 6

def horas_trabalhadas(segunda, terça, quarta, quinta, sexta):
    dicionario = dict(Segunda= segunda,Terça= terça, Quarta= quarta, Quinta= quinta, Sexta= sexta)
    soma = dicionario.values()
    print(f'{sum(soma)} horas trabalhadas.')
    
horas_trabalhadas(8, 9, 6, 7, 9)

# Exercicio 7

alunos = ['Yan', 9, 'Filipe', 9, 'Jairo', 8, 'Renan', 8.5]

chave = (alunos[::2])
valor = (alunos[1::2])
# print(chave, valor)

dic = dict(zip(chave, valor))     
print(dic)

def buscar_aluno(aluno):
    for i in dic:
        if i == aluno:
            print(f'Aluno: {i} - Nota: {dic[i]}')
            
buscar_aluno('Jairo')

def atualizar_nota(aluno, nota):
    if aluno in dic.keys():
        dic.update({aluno: nota})
        print(dic)
    else:
        print(f'O(a) Aluno(a) {aluno} não está na lista')
atualizar_nota('Jairo', 5)

# Exercicio 8

produtos = {'Martelos': 5, 'Cimentos': 34, 'Tijolos': 670, 'Ferragens': 12, 'Pás': 7}

def produto(produto):
        if produto in produtos.keys():
            print(f'{produtos[produto]} {produto} disponiveis.')
        elif produto not in produtos.keys():
            print('Não esta em estoque.')

produto('Martelos')

# Exercicio 9

paises = [ 'Brasil', 'Chile', 'Estados Unidos', 'França']
capital = ['Brasilia', 'Santiago', 'Washington', 'Paris' ]

dicionario_paises = dict(zip(paises, capital))
print(dicionario_paises)

# Exercicio 10


estudantes = {}

def add_alunos(aluno,nota1, nota2, nota3):
    notas = dict(português= nota1, matematica= nota2, ciencias= nota3)
    estudantes.update({aluno: notas}) 
    
add_alunos('yan', 7.5, 8, 10)
add_alunos('filipe', 7, 8.5, 9)


def alterar_notas(aluno):
    print(estudantes)
    for estudante in estudantes.keys():
        if estudante == aluno:
            nota1 = float(input(f'Atualize a nota de portugues do(a) aluno(a) {aluno}: '))
            nota2 = float(input(f'Atualize a nota de matematica do(a) aluno(a) {aluno}: '))
            nota3 = float(input(f'Atualize a nota de ciencias do(a) aluno(a) {aluno}: '))
            add_alunos(aluno, nota1, nota2, nota3)
            
alterar_notas('filipe')
print(estudantes)           

# Exercicio 11

numeros = [26, 56 , 51, 78, 23, 89, 90, 45, 34, 32, 39, 70]

def soma_pares(lista):
    soma = 0
    for numero in lista:
        if numero % 2 == 0:
            soma += numero
    return soma
result = soma_pares(numeros)
print(result)


# Exercicio 12

produtos = {
    'bola': 150.0,
    'notebook': 3200.0,
    'mochila': 78.0,
    'caderno': 25.0
    }

def produto_caro(lista):
    max_valor = max(lista.values())
    chave = [x for x in lista if lista[x] == max_valor]
    if len(chave) > 1:
        print(f"Os produtos mais caros são {', '.join(chave)} custando R$ {max_valor}")
    else:
        print(f"O produto mais caro é o(a) {''.join(chave)}  custando R$ {max_valor}.")
            
produto_caro(produtos)


# Exercicio 13

lista = [34, 56, 79, 51, 13, 84]

def multiplicar(lista, n=None):
    if n == None:
        return lista
    result = [x * n for x in lista]
    return result
res = multiplicar(lista, 2)
print(res)    


# Exercicio 14

produtos = {'bola': 7,'notebook': 3,'mochila': 4,'caderno': 11}

def verificar_estoque(lista, item, quant):
    if item in lista.keys(): 
        if produtos[item] < quant:
            print(f'Não há {item} em estoque.')
        else:
            produtos[item] = ((produtos[item] - quant))
    else:
        print('Produto não encontrado.')
            
verificar_estoque(produtos, 'mochila', 2)
print(produtos)

# Exercicio 15
alunos = [{'Yan': [6, 8, 7]}, {'Filipe': [4, 10, 8]}, {'Jairo': [5, 9, 6]}]
media_aluno = {}

def media(lista):
    for aluno in lista:
        for i in aluno:
            nota = (f'{sum(aluno[i])/len(aluno[i]):.1f}')
            media_aluno.update({i : nota})
    
media(alunos)
print(media_aluno)
        
        

# Exercicio 16

numeros= [10, 23 ,25, 32, 43, 45, 56, 59, 67, 72, 81]
chave = 59

def busca_binaria(lista, chave, inicio=0, fim=None):
    if fim is None:
        fim = len(lista) -1     # = 10
    
    if inicio > fim:    # Não está na lista
        return -1
    
    meio = (inicio + fim)//2    # 0 + 10 // 2 == 5 || # 6 + 10// 2 == 8 || # 6 + 7 // 2 == 6 || # 7 + 7 // 2 == 7
    if lista[meio] == chave: # lista[5] || lista[8] || lista[6]
        return meio     # Se o numero da lista[5](45) == chave (59) ele retorna o indice.
                        # Se o numero da lista[8](67) == chave (59) ele retorna o indice.
                        # Se o numero da lista[6](56) == chave (59) ele retorna o indice.
                        # Se o numero da lista[7](59) == chave (59) ele retorna o indice.
                        # Ele vai retornar o numero 7.
                        
    if lista[meio] > chave: # 45 é menor que 59, então ele NÃO SE ENCAIXA nesse if
                            # 67 é maior que 59, então ele SE ENCAIXA nesse if
                            # 56 é menor que 59, então ele NÃO SE ENCAIXA nesse if
        return busca_binaria(lista, chave, inicio, meio -1) # Meio - 1 == 8-1 == 7, o fim passa a ser 7 agora e retorna ao topo do def.
    
    if lista[meio] < chave: # 45 é menor que 59, então ele SE ENCAIXA nesse if
                            # 67 é maior que 59, então ele NÃO SE ENCAIXA nesse if
                            # 56 é menor que 59, então ele SE ENCAIXA nesse if
        return busca_binaria(lista, chave, meio +1, fim)  # Meio +1 == 5 + 1 == 6, o inicio passa a ser 6 agora e retorna ao topo do def.
                                                          # Meio +1 == 6 + 1 == 7, o inicio passa a ser 7 agora e retorna ao topo do def.


resultado = busca_binaria(numeros, chave)

if resultado != -1:
    print(f"Numero encontrado no índice: {resultado}")
else:
    print("Numero não encontrado.")



    
    
    







    

    
    
 



        
        

        

        

    




    

        
        



   
