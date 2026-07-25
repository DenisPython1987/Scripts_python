from Desafio_115 import cadastro
import Desafio_113
nome = str(input("Digite seu nome: "))
idade = Desafio_113.leia_int("Digite sua idade: ")

dados = cadastro.cadastrar(nome, idade)
cadastro.gravar(dados)
resultado = cadastro.ler_arquivo("Desafio_115.txt")
print(resultado)