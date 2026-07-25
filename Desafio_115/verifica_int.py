def verifica_inteiro(mensagem):
    while True:
        número = str(input(mensagem))
        if número.isnumeric():
            return número
        else:
            print("\033[31mNúmero inválido. Tente novamente.\033[m")
            continue