def maior(*números):
    return max(números)


escolha = ''
lista = list()
while True:
    try:
        número = int(input("\033[36mDigite um número: \033[m"))
        lista.append(número)
        while True:
            try:
                escolha = str(input("\033[35mQuer continuar? [S/N]: \033[m")).strip().upper()[0]
                if escolha not in "SN":
                    print("\033[31mEscolha inválida! Digite apenas S ou N.\033[m")
                    continue
                if escolha in "SN":
                    break
            except IndexError:
                print("\033[31mSua opção não pode estar vazia! Digite apenas S ou N.\033[m")
                continue
        if escolha == "N":
            break
    except ValueError:
        print("\033[31mValor inválido! Digite apenas números inteiros!\033[m")
        continue

maior_número = maior(*lista)
print(f"\033[33mO maior número fornecido foi\033[m \033[36m {maior_número}\033[m")