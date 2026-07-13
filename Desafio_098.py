from time import sleep

escolha = ''

print("\033[35m-*-\033[m" * 20)
print(f"{'\033[35mContador':^60}\033[m")
print("\033[35m-*-\033[m" * 20)

def contador(início, fim, passo):
    if passo == 0:
        passo = 1
    if início < fim:
        for i in range(início, fim + 1, passo):
            print(f"\033[36m{i}\033[m", end=" ")
            sleep(1)
        print()
    elif fim < início:
        if passo > 0:
            passo *= -1
        for i in range(início, fim - 1, passo):
            print(f"\033[36m{i}\033[m", end=" ")
            sleep(1)
        print()

print("\033[36m-=-\033[m" * 20)
print(f"\033[36m{'Contando de 1 até 10':^60}\033[m")
print("\033[36m-=-\033[m" * 20)
contador(1, 10, 1)
print("\033[36m-=-\033[m" * 20)
print(f"\033[36m{'Contando de 10 até 0 de 2 em 2':^60}\033[m")
print("\033[36m-=-\033[m" * 20)
contador(10, 0, 2)

while True:
    try:
        início = int(input("\033[32mDigite o início: "))
        fim = int(input("Digite o fim: "))
        passo = int(input("Digite o passo: \033[m"))
        contador(início, fim, passo)
        while True:
            try:
                escolha = str(input("\033[33mQuer continuar? [S/N]: \033[m")).strip().upper()[0]
                if escolha not in "SN":
                    print("\033[31mEscolha inválida! Digite apenas S ou N.\033[m")
                    continue
                if escolha in "SN":
                    break
            except IndexError:
                print('\033[31mSua escolha não pode ficar vazia! Tente novamente!\033[m')
                continue
        if escolha == "N":
            break
    except ValueError:
        print("\033[31mValor inválido! Digite apenas números inteiros.\033[m")
        continue

print("\033[35m-*-\033[m" * 20)
print(f"\033[35m{'Volte sempre':^60}\033[m")
print("\033[35m-*-\033[m" * 20)