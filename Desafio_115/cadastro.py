def cadastrar(nome, idade):
    return [nome,idade]

def gravar(lista):
    with open("Desafio_115.txt", "a", encoding='utf-8') as arquivo:
        arquivo.write(f"{lista[0]}; {lista[1]}\n")

def ler_arquivo(arquivo):
    pessoa = []
    with open(arquivo, 'r', encoding='utf-8') as arquivo:
        for linhas in arquivo:
            dados = linhas.strip().split(';')
            pessoa.append(dados)
        return pessoa