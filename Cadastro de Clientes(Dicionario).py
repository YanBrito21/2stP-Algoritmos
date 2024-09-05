clientes = []
def adicionar_cliente(nome,email, telefone, endereco):
    cliente = {
    'Nome' : nome,
    'E-mail' : email,
    'Telefone' : telefone,
    'Endereço' : endereco
    }
    for Cliente in clientes:
        if Cliente.get('E-mail') == email:
            print('O E-mail deste cliente já existe no sistema.')
            return
    clientes.append(cliente)
adicionar_cliente('Yan','yan@gmail.com', '9999', 'Rua A')
adicionar_cliente('Filipe', 'filipe@gmail.com', '8888', 'Rua B')

def exibir_cliente():
    for cliente in clientes:
        res = ('Nome:', cliente.get('Nome'),'-', 'E-mail:', cliente.get('E-mail'), '-', 'Telefone:', cliente.get('Telefone'),'-', 'Endereço:', cliente.get('Endereço'))
        res = ' '.join(res)
        print(res)
# exibir_clientes()

def buscar_cliente(email):
    for cliente in clientes:
        if cliente.get('E-mail') == email:
            res = ('Nome:', cliente.get('Nome'),'-', 'E-mail:', cliente.get('E-mail'), '-', 'Telefone:', cliente.get('Telefone'),'-', 'Endereço:', cliente.get('Endereço'))
            res = ' '.join(res)
            print('Cliente encontrado!')
            print(res)
            return
    print(f'Cliente {email} não encontrado.')    

# buscar_cliente('filipe@gmail.com')

def remover_cliente(email):
    for cliente in clientes:
        if cliente.get('E-mail') == email:
            res = ('Cliente',' "',cliente.get('Nome'), '" ','removido!')
            res = ''.join(res)
            print(res)
            clientes.remove(cliente)
            
# remover_cliente('filipe@gmail.com')

while True:
    escolha = input('O que você deseja? digite [E] para [Exibir clientes], [A] para [Adicionar clientes], [B] para [Buscar clientes], [R] para [Remover clientes] ou [S] para [Sair do menu]: ')
    if escolha.upper() == 'A':
        nome = input('Digite o nome do cliente: ')
        email = input('Digite o e-mail do cliente: ')
        telefone = input('Digite o telefone do cliente: ')
        endereco = input('Digite o endereço do cliente: ')
        adicionar_cliente(nome, email, telefone, endereco)
        
    elif escolha.upper() == 'E':
        exibir_cliente()

    elif escolha.upper() == 'B':
        email = input('Digite o e-mail para buscar o cliente: ')
        buscar_cliente(email)
        
    elif escolha.upper() == 'R':
        email = input('Digite o e-mail para remover o cliente: ')
        remover_cliente(email)

    elif escolha.upper() == 'S':
        break
    else:
        print('Resposta incorreta.')
