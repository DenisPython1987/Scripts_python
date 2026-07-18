
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
    dicionário_notas['média'] = f'{média:.2f}'
    if show:
        if média >= 7:
            dicionário_notas['situação'] = "boa"
        elif média >= 6:
            dicionário_notas['situação'] = "razoável"
        else:
            dicionário_notas['situação'] = "ruim"
    return dicionário_notas
teste = ()
resultado = notas(1, 7, 5.5, 10, 8, 9, 9.7, 6.5, show=True)
print(resultado)
resultado_2 = notas(5, 5.5, 6.7, 7.2, 1.2, 2.3, 4.4, show=True)
print(resultado_2)