def apresentação(mensagem):
    print("\033[35m-*-\033[m" * 20)
    print(f"\033[35m{mensagem:^60}\033[m")
    print("\033[35m-*-\033[m" * 20)


def sorteia():
    from random import randint
    from time import sleep
    lista = list()
    for i in range(0, 5):
        número = randint(1, 10)
        lista.append(número)
        if número % 2 == 0:
            cor = "\033[36m"
        else:
            cor = "\033[31m"
        print(f"{cor}{número}\033[m", end=' ')
        sleep(1)
    print()
    return lista


def somapar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    if soma == 0:
        return 0
    else:
        return soma
apresentação("Sorteando os números!")
valores = sorteia()
soma = somapar(valores)

print(f"\033[35mA soma dos valores pares é {soma}\033[m.")