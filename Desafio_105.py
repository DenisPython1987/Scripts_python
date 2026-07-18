from Desafio_090 import situação


def notas(* n, show=False):
    maior = soma = menor = 0
    dicionário_notas = dict()
    for indice, nota in enumerate(n):
        if indice == 0:
            maior = menor = nota
        if nota > maior:
            maior = nota
        elif nota < menor:
            menor = nota
        soma += nota
    média = soma / len(n)
    dicionário_notas['quantidade_notas'] = len(n)
    dicionário_notas['maior_nota'] = maior
    dicionário_notas['menor_nota'] = menor
    dicionário_notas['média'] = média
    if show:
        if média >= 7:
            dicionário_notas['situação'] = "boa"
        elif média >= 6:
            dicionário_notas['situação'] = "razoável"
        else:
            dicionário_notas['situação'] = "ruim"
    return dicionário_notas
