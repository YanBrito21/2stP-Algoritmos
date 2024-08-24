clientes = []
def adicionar_cliente(nome, email, telefone, endereço):
    cliente = (nome, email, telefone, endereço)
    clientes.append(list(cliente))

# adicionar_cliente('Yan','yan@gmail.com', '9999', 'Rua A')
# adicionar_cliente('Filipe', 'filipe@gmail.com', '8888', 'Rua B')


def exibir_cliente ():
    for i in clientes:
        print(f'Cliente: {i[0]} - Email: {i[1]} - Telefone: {i[2]} - Endereço: {i[3]}')
# exibir_cliente()

def buscar_cliente(email):
    for cliente in clientes:
        if email in cliente:
            print(f'Cliente: {cliente[0]} \nEmail: {cliente[1]} \nTelefone: {cliente[2]} \nEndereço: {cliente[3]}')        
# buscar_cliente('yan@gmail.com')

def remover_cliente(email):
    for cliente in clientes:
        if email in cliente:
            print(f'cliente {cliente[0]} removido com sucesso!')
            clientes.remove(cliente)
# remover_cliente('filipe@gmail.com')


while True:
    escolha = input('O que você deseja? digite [E] para [Exibir clientes], [A] para [Adicionar clientes], [B] para [Buscar clientes], [R] para [Remover clientes] ou [S] para [Sair do menu]: ')
    if escolha.upper() == 'A':
        nome = input('Digite o nome do cliente: ')
        email = input('Digite o e-mail do cliente: ')
        telefone = input('Digite o telefone do cliente: ')
        endereço = input('Digite o endereço do cliente: ')
        adicionar_cliente(nome, email, telefone, endereço)
        
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


