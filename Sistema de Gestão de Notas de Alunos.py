# Sistema de Gestão de Notas de Alunos #

alunos = [ {'Nome': 'Filipe', 'Notas': [8.0, 7.0], 'Media': 7.5}, {'Nome': 'Yan', 'Notas': [10.0, 9.0], 'Media': 9.5}, {'Nome': 'Jairo', 'Notas': [9.0, 4.0], 'Media': 6.5}]

def adicionar_aluno():
    Nome = input("Digite o nome do aluno(a): ")
    Notas = []
    qnt = 5
    while True:
        try:
            if qnt == 0:
                break
            nota = input("Digite as notas do aluno(a). Caso não tenha notas a adicionar, digite [00] para parar: ")
            if nota == "00":
                if len(Notas) <1:
                    print("Digite no mínimo duas notas.")
                elif len(Notas) <2:
                    print("Digite mais uma nota.")
                else:
                    break
            elif nota.isnumeric():
                nota_float = float(nota)
                if nota_float < 10.1:
                    Notas.append(float(nota))
                    qnt -=1
                else:
                    raise ValueError("Digite apenas números entre 0 e 10.")
            else:
                raise ValueError("Digite APENAS numeros para adicionar as notas. OU [!] para parar.")   
        except Exception as e:
            print(e)
        except ValueError:
            print("Erro value error")
            
    aluno = {
        "Nome" : Nome,
        "Notas": Notas,
        "Media": sum(Notas) / len(Notas)
    }
    alunos.append(aluno)

# adicionar_aluno()

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j]["Media"] < key["Media"]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def ordenar_alunos ():
    insertion_sort(alunos)
       
# ordenar_alunos()
import os
def salvar(local_do_arquivo):
    try:
        with open(local_do_arquivo, "w") as SistemaDeNotas:
            for aluno in alunos:
                SistemaDeNotas.write(f"Nome do Aluno(a):{aluno['Nome']}\nNotas: {aluno['Notas']}\n")
            SistemaDeNotas.write(f"\nAlunos ordenados por Média:\n\n")
            ordenar_alunos()
            for aluno in alunos:
                SistemaDeNotas.write(f"{aluno['Nome']} - Média: {aluno['Media']:.1f}\n")
        with open(local_do_arquivo, "r") as SistemaDeNotas:
            texto = SistemaDeNotas.read()
        print(texto)
        print(f"Os dados foram salvos no arquivo {local_do_arquivo}.")
    except FileNotFoundError:
        print("Arquivo não encontrado. \nVerifique se o caminho do arquivo está correto.")
        
def salvar_em_arquivo(local_do_arquivo):
    try:
        if os.path.exists(local_do_arquivo):
            print("O arquivo já existe.")
            esc = input("Digite [1] para sobrescrever os dados OU qualquer tecla para cancelar: ")
            if esc == "1":
                salvar(local_do_arquivo)
            else:
                print("Execução cancelada.")
        else:       
            salvar(local_do_arquivo)
    except PermissionError:
        print("Você não tem permissão para salvar este arquivo.")
    except FileNotFoundError:
        print("Arquivo não encontrado. \nVerifique se o caminho do arquivo está correto.")
    except OSError:
        print("Sem espaço no dispositivo.")

while True:
    menu = input("[1] para Adicionar alunos. \n[2] para Ordenar alunos. \n[3] para Salvar em arquivo. \n[4] para sair. \n ")
    try:
        if menu == "1":
            adicionar_aluno()
        elif menu == "2":
            ordenar_alunos()
        elif menu == "3":
            local_do_arquivo = input("Digite o nome ou local do arquivo: ")
            salvar_em_arquivo(local_do_arquivo)
        elif menu == "4":
            print("Programa encerrado.")
            break
        else:
            raise ValueError
    except ValueError:
        print("Escolha inválida, digite apenas 1, 2, 3 ou 4.")


