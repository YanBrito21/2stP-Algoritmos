livros = []

def cadastrar_livro(titulo, autor, genero,quant,codigo):
    livros.append({'Titulo': titulo,
                   'Autor' : autor,
                   'Genero': genero,
                   'Quant': quant,
                   'Codigo': codigo
                   })

cadastrar_livro('O segredo', 'Paul Heink', 'Terror', 5, 345)
cadastrar_livro('O fim', 'Julia Robert', 'Romance', 3, 216)
cadastrar_livro('O caminho desconhecido', 'Vlad Dameron', 'Aventura', 7, 567)


def buscar_livro(codigo):
    for livro in livros:
        if codigo == livro['Codigo']:
            print(f"Titulo: {livro['Titulo']} | Autor: {livro['Autor']} | Genero: {livro['Genero']} | Quantidade: {livro['Quant']} | Codigo: {livro['Codigo']}")
    
buscar_livro(216)


def atualizar_livro(codigo, quant):
    for livro in livros:
        if codigo == livro["Codigo"]:
            livro["Quant"] = quant

atualizar_livro(216, 5)


def remover_livro(codigo):
    for livro in livros:
        if codigo == livro["Codigo"]:
            livro["Quant"] = livro["Quant"] -1

remover_livro(567)


def listar_livros():
    for livro in livros:
        print(f"Titulo: {livro['Titulo']} | Autor: {livro['Autor']} | Genero: {livro['Genero']} | Quantidade: {livro['Quant']} | Codigo: {livro['Codigo']}")

listar_livros()