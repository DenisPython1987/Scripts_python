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

def resumo(valor, aumentando, diminuindo):
    print(f"O preço de {moeda(valor)} aumentado é {aumentar(valor, aumentando, True)}.")
    print(f"O preço de {moeda(valor)} diminuído é {diminuir(valor, diminuindo, True)}.")
    print(f"O dobro de {moeda(valor)} é {dobro(valor, True)}.")
    print(f"A metade de {moeda(valor)} é {metade(valor, True)}.")