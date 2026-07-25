import cadastro
import opções
import menu
import apresentação
import verifica_int

while True:
    apresentação.cabeçalho("CADASTRO DE PESSOAS")
    menu.menu()
    opção = opções.escolha()
    if opção == 1:
        apresentação.cabeçalho("CADASTRO")
        nome = str(input("\033[36mDigite seu nome: \033[m"))
        idade = verifica_int.verifica_inteiro("\033[36mDigite sua idade: \033[m")
        dados = cadastro.cadastrar(nome, str(idade))
        cadastro.gravar(dados)
    elif opção == 2:
        apresentação.cabeçalho("PESSOAS CADASTRADAS")
        resultado = cadastro.ler_arquivo("Desafio_115.txt")
        for pessoa in resultado:
            print(f"\033[34m{pessoa[0]:.<40}{pessoa[1]:^5}anos\033[m")
    elif opção == 3:
        break
apresentação.cabeçalho("FIM DO PROGRAMA")
