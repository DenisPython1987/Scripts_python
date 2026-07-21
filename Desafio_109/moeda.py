def aumentar(valor, porcentagem, show=False):
    final = valor + (valor * porcentagem / 100)
    if show:
        return moeda(final)
    else:
        return final


def diminuir(valor, porcentagem, show=False):
    final = valor - (valor * porcentagem / 100)
    if show:
        return moeda(final)
    else:
        return final

def dobro(valor, show=False):
    final = valor * 2
    if show:
        return moeda(final)
    else:
        return final

def metade(valor, show=False):
    final = valor / 2
    if show:
        return moeda(final)
    else:
        return final

def moeda(valor):
    return f'R${valor:.2f}'.replace('.', ',')