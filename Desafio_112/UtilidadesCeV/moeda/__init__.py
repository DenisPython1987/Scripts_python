def aumentar(valor, porcentagem, show=False):
    """
    Função para aumentar um valor com base num percentual.
    :param valor: Valor a ser aumentado.
    :param porcentagem: Percentual a ser aumentado.
    :param show: Parâmetro opcianl para formatação em moeda.
    :return: Valor aumentado, em moeda ou não.
    """
    final = valor + (valor * porcentagem / 100)
    if show:
        return moeda(final)
    else:
        return final


def diminuir(valor, porcentagem, show=False):
    """
    Função para diminuir um valor com base num percentual.
    :param valor: Valor a ser diminuído.
    :param porcentagem: Percentual a diminuir.
    :param show: Parâmetro opcional para mostrar formatação em moeda.
    :return: Valor diminuído, em moeda ou não
    """
    final = valor - (valor * porcentagem / 100)
    if show:
        return moeda(final)
    else:
        return final

def dobro(valor, show=False):
    """
    Função para dobrar um valor qualquer.
    :param valor: Valor a ser dobrado.
    :param show: Parâmetro opcional para formatar em moeda.
    :return: Valor sobrado, em moeda ou não.
    """
    final = valor * 2
    if show:
        return moeda(final)
    else:
        return final

def metade(valor, show=False):
    """
    Função para dividir um valor em dois.
    :param valor: Valor a ser dividido.
    :param show: Parâmetro opcional para formatar em moeda.
    :return: Valor dividido por dois, em moeda ou não.
    """
    final = valor / 2
    if show:
        return moeda(final)
    else:
        return final

def moeda(valor):
    """
    Função para formatar um valor em moeda..
    :param valor: Valor a ser formatado.
    :return: Valor no formato de moeda.
    """
    return f'R${valor:.2f}'.replace('.', ',')

def resumo(valor, aumentando, diminuindo):
    """
    Função para resumir as transformações do valor dado.
    :param valor: Valor a ser resumido.
    :param aumentando: Percentual a aumentar.
    :param diminuindo: Percentual a diminuir.
    :return: Quatro prints com o resumo das transformações.
    """
    print(f"O preço de {moeda(valor)} aumentado "
          f"em {aumentando}% é {aumentar(valor, aumentando, True)}.")
    print(f"O preço de {moeda(valor)} diminuído "
          f"em {diminuindo}% é {diminuir(valor, diminuindo, True)}.")
    print(f"O dobro de {moeda(valor)} é {dobro(valor, True)}.")
    print(f"A metade de {moeda(valor)} é {metade(valor, True)}.")