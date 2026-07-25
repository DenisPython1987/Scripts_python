def cadastrar(nome, idade):
    return [nome,idade]

def gravar(lista):
    with open("Desafio_115.txt", "a", encoding='utf-8') as arquivo:
        for indice, linha in enumerate(lista):
            arquivo.write(linha, end='')
            if indice == 1:
                arquivo.write('\n')

def ler_arquivo(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        return linhas