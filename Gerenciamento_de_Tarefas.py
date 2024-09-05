
lista_tarefas = []

def adicionar_tarefa(lista_tarefas, descricao, status, prioridade):
    if not lista_tarefas:
        id = 1
    else:
        id = max(tarefa['id'] for tarefa in lista_tarefas)+1
    tarefa = {
    'id' : id,
    'descricao' : descricao,
    'status' : status,
    'prioridade' : prioridade
    }
    lista_tarefas.append(tarefa)
adicionar_tarefa(lista_tarefas,'Trabalho de Algoritmos', 'pendente','alta')
adicionar_tarefa(lista_tarefas,'Exercicio de Web Sites', 'concluido','media')
adicionar_tarefa(lista_tarefas,'Ler um livro', 'concluido','baixa')
adicionar_tarefa(lista_tarefas,'Estudar Java', 'pendente','media')

def visualizar_tarefas(lista_tarefas):
    for tarefas in lista_tarefas:
        print(f'ID: {tarefas["id"]} - Descrição: {tarefas["descricao"]} - Status: {tarefas["status"]} - Prioridade: {tarefas["prioridade"]}')
        
#visualizar_tarefas(lista_tarefas)

def filtrar_tarefas(lista_tarefas, status=None, prioridade=None):
    filtro_tarefas = [chave for chave in lista_tarefas if (status is None or status == chave['status']) and (prioridade is None or prioridade == chave['prioridade'])]
    if not filtro_tarefas:
        visualizar_tarefas(lista_tarefas)
        return
    for filtro in filtro_tarefas:
        print(f'ID: {filtro["id"]} - Descrição: {filtro["descricao"]} - Status: {filtro["status"]} - Prioridade: {filtro["prioridade"]}')
    
filtrar_tarefas(lista_tarefas,status="pendente",prioridade=None)



  
    
