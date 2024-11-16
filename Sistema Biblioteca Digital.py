livros =[]

def adicionar_livro(titulo, autor, ano, paginas):
    livro = dict(Titulo=titulo, Autor=autor, Ano=int(ano), Paginas=int(paginas))
    livros.append(livro)
    print("Livro adicionado com sucesso!")
adicionar_livro("Futebol Magico", "Giorgian De Arrascaeta", 2003, 137)
adicionar_livro("P9 Queixada", "Pedro Nine", 2012, 90)
adicionar_livro("Meu amigao", "José Phillips", 2001, 171)

def listar_livros(livros):
    for livro in livros:
        print(f"Titulo: {livro['Titulo']} \nAutor: {livro['Autor']} \nAno: {livro['Ano']} \nPaginas: {livro['Paginas']}\n")

def Quick_Sort(lista, n):
    if len(lista) > 1:
        divisao = len(lista) // 2
        valor = lista[divisao]
        esquerda = [num for num in lista if num[n] < valor[n]]
        meio = [num for num in lista if num[n] == valor[n]]
        direita = [num for num in lista if num[n] > valor[n]]
        
        res = Quick_Sort(esquerda,n) + meio + Quick_Sort(direita,n)
        return res
    else:
        return lista
    
def ordenar_livros():
    while True:
        print("[1] para ordenar por Ano \n[2] para ordenar por numero de Paginas.")
        try:
            escolha = input()
            if escolha == "1":
                print("[1] para ordem Crescente. \n[2] para ordem Decrescente.")
                menu = input("")
                while menu != "1" and menu != "2":
                    print("Digite apenas:")
                    print("[1] para ordem Crescente. \n[2] para ordem Decrescente.")
                    menu = input("")
                if menu == "1":
                    res = Quick_Sort(livros, 'Ano')
                    for i in range (len(livros)):
                        livros[i] = res[i]
                    break
                elif menu == "2":
                    res = Quick_Sort(livros, 'Ano')
                    result = list(reversed(res))
                    for i in range (len(livros)):
                        livros[i] = result[i]
                    break
            elif escolha == "2":
                print("[1] para ordem Crescente. \n[2] para ordem Decrescente.")
                menu = input("")
                while menu != "1" and menu != "2":
                    print("Digite apenas:")
                    print("[1] para ordem Crescente. \n[2] para ordem Decrescente.")
                    menu = input("")
                if menu == "1":
                    res = Quick_Sort(livros, 'Paginas')
                    for i in range (len(livros)):
                        livros[i] = res[i]
                    break
                elif menu == "2":
                    res = Quick_Sort(livros, 'Paginas')
                    result = list(reversed(res))
                    for i in range (len(livros)):
                        livros[i] = result[i]
                    break
            else:   
                raise ValueError     
        except ValueError:
            print("Digite apenas [1] ou [2].")
import os
import platform

def salvar(local_arquivo):
    with open(local_arquivo, 'w') as biblioteca:
        for livro in livros:
            biblioteca.write(f"Titulo: {livro['Titulo']}, Autor: {livro['Autor']}, Ano: {livro['Ano']}, Paginas: {livro['Paginas']}\n\n")
    print(f"Os dados foram salvos no arquivo {local_arquivo}.")
def salvar_livros(local_arquivo):
    try:
        if os.path.exists(local_arquivo):
            print("O arquivo já existe.")
            escolha = input("Digite [S] para sobrescrever os dados ou qualquer outra tecla para cancelar.\n")
            if escolha.upper() == "S":
                salvar(local_arquivo)
            else:
                print("Execução cancelada.")
        else:
            salvar(local_arquivo)
    except PermissionError:
        print("Você não tem permissão para salvar este arquivo.")
    except FileNotFoundError:
        print("Arquivo não encontrado. \nVerifique se o caminho do arquivo está correto.")
    except OSError:
        print("Sem espaço no dispositivo.")
        
def carregar_livros(local_arquivo):
    try:
        with open(local_arquivo, "r") as biblioteca:
            texto = biblioteca.read()
            print(texto)
    except FileNotFoundError:
        print("Arquivo não encontrado. \nVerifique se o caminho do arquivo está correto.")
        
def limpar():
    if platform.system() == "Windows":
        os.system("cls") 
    else:
        os.system("clear")      

while True:
    print("Escolha uma opção: \n[1] Adicionar livro \n[2] Listar livros \n[3] Ordenar livros \n[4] Salvar dados em arquivo \n[5] Carregar dados do arquivo \n[6] Sair")
    menu = input("")
    if menu == "1":
        limpar()
        titulo = input('Digite o Titulo do livro: ')
        autor = input('Digite o Autor do livro: ')
        while True:
            try:
                ano = int(input('Digite o Ano do livro: '))
                break
            except ValueError:
                print('Nas opções "Ano" e "Paginas". Digite apenas numeros inteiros e positivos por favor.')
        while True:
            try:
                paginas = int(input('Digite o numero de paginas do livro: '))
                break
            except ValueError:
                print('Nas opções "Ano" e "Paginas". Digite apenas numeros inteiros e positivos por favor.')
        adicionar_livro(titulo, autor, ano, paginas)
    
    elif menu == "2":
        limpar()
        listar_livros(livros)
    elif menu == "3":
        limpar()
        ordenar_livros()
    elif menu == "4":
        limpar()
        local_arquivo = input("Digite o nome ou local do arquivo: ")
        salvar_livros(local_arquivo)
    elif menu == "5":
        limpar()
        local_arquivo = input("Digite o nome ou local do arquivo: ")
        carregar_livros(local_arquivo)
        
    elif menu == "6":
        limpar()
        try:
            escolha = input("Deseja salvar os dados antes de sair? (S/N): ")
            if escolha.upper() == "S":
                local_arquivo = input("Digite o nome ou local do arquivo: ")
                salvar_livros(local_arquivo)
                break
            elif escolha.upper() == "N":
                print("Programa encerrado!")
                break
            else:
                raise ValueError
        except ValueError:
            print("Digite apenas [S] ou [N].")
        
        
        
    