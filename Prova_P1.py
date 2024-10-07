
projetos = []

def cadastrar_projeto(codigo, cliente, gerente, data, status):
    projetos.append({'Codigo': codigo,
                     'Cliente' : cliente,
                     'Gerente': gerente,
                     'Data': data,
                     'Status': status
    })

cadastrar_projeto("P001", "Cliente A", "Gerente X", "2024-01-01",
"Planejamento")
cadastrar_projeto("P002", "Cliente B", "Gerente Y", "2024-02-01", "Em Andamento")
cadastrar_projeto("P003", "Cliente A", "Gerente X", "2024-03-01", "Concluído")


def atualizar_status_projeto(codigo, status):
    for projeto in projetos: 
        if codigo == projeto['Codigo']:
            projeto['Status'] = status
            return
    print(f'O código {codigo} não existe!')

# atualizar_status_projeto('P005', 'Concluído')


def buscar_projeto(codigo):

    for projeto in projetos:
        for i, v in enumerate(projeto):
            if codigo == projeto[v]:
                print(f"Código do projeto: {projeto['Codigo']}\nCliente: {projeto['Cliente']}\nGerente: {projeto['Gerente']}\nData: {projeto['Data']}\nStatus: {projeto['Status']}")
                return

    print(f'O projeto com o código {codigo} não foi encontrado.')

    return
# buscar_projeto('P003')


def listar_projetos():
    if len(projetos) > 0:
        for projeto in projetos:
            print((f"Código: {projeto['Codigo']} | Cliente: {projeto['Cliente']} | Gerente: {projeto['Gerente']} | Data: {projeto['Data']} | Status: {projeto['Status']}"))
    else:
        print('Não há projetos disponíveis.')

# listar_projetos()


def contar_projetos_por_gerente(gerente):
    contagem = 0
    for produto in projetos:
        if gerente == produto['Gerente']:
            contagem += 1
    print(f' O(A) {gerente} possui {contagem} projetos cadastrados.')

# contar_projetos_por_gerente('Gerente X')



while True:
    menu =  input("escolha [1] para para cadastrar projeto, [2] para buscar projeto, [3] para atualizar status do projeto, [4] para listar projetos, [5] para contar projetos por gerente, [6] para sair: ")
    
    if menu == "1":
        codigo = input("Digite o número do código do projeto: ")
        cliente = input("Digite o nome do cliente do projeto: ")
        gerente = input("Digite o nome do gerente do projeto: ")
        data = input("Digite a data do projeto: ")
        status = input("Digite o status do projeto: ")
        cadastrar_projeto(codigo, cliente, gerente, data, status)
    
    elif menu == "2":
        codigo = input("Digite o número do código: ")
        buscar_projeto(codigo)
        
    elif menu == "3":
        codigo = input("Digite o código do projeto: ")
        status = input("Digite o novo status do projeto: ")
        atualizar_status_projeto(codigo, status)
        
    elif menu == "4":
        listar_projetos()
        
    elif menu == "5":
        gerente = input("Digite o nome do gerente: ")
        contar_projetos_por_gerente(gerente)
        
    elif menu == "6":
        break
        