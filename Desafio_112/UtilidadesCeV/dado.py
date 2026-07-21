def leia_dinheiro(mensagem):
    """
    Função para ler valores monetários.
    :param mensagem: string que pode ser xx.xx, ou xx,xx.
    :return: Valor já formatado como float.
    """
    while True:
        número = str(input(mensagem))
        parcial = número.replace(',', '')
        if parcial.isnumeric():
            return float(número.replace(',', '.'))
        else:
            print(f'"{número}" não é um número válido. Digite um valor real.')
            continue