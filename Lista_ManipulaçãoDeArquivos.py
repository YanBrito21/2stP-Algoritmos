"""1. Ler um Arquivo de Texto
 - Crie um arquivo de texto chamado `mensagem.txt` com algumas linhas de texto.
 - Escreva um programa que leia todo o conteúdo desse arquivo e o exiba no console."""

with open('mensagem.txt', 'w') as mensagem:
    mensagem.write("Olá, Bom dia! \n")
    mensagem.write("Seja muito bem vindo a Saquarema. \n")
    mensagem.write("Saquarema é conhecida como a “Capital Nacional do Surfe”, sendo recorrentemente a etapa brasileira do WSL (Surf World League)\ne a “Casa do Vôlei Brasileiro”, por ser a sede da Confederação Brasileira de Voleibol (CBV).\nDestaca-se pelas suas belas praias, lagoas, cachoeiras e montanhas. \n")

with open('mensagem.txt', 'r') as mensagem:
    texto = mensagem.read()
    print(texto)

"""2. Escrever em um Arquivo de Texto
 - Crie um programa que peça ao usuário para digitar uma frase.
 - Escreva essa frase em um novo arquivo chamado `frase_usuario.txt`."""

with open('frase_usuario.txt', 'w') as mensagem:
    usuario = input("Digite aqui: ")
    mensagem.write(f"{usuario}\n")

# with open('frase_usuario.txt', 'r') as mensagem:
    # texto = mensagem.read()
    # print(texto)

"""3. Contar Linhas e Palavras
 - Escreva um programa que leia o conteúdo de um arquivo `texto.txt`.
 - Conte quantas linhas e palavras o arquivo possui e exiba esses valores no console."""




