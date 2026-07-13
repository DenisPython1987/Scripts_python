
def área(largura, comprimento):
    return largura * comprimento

escolha = ""

while True:
    try:
        largura = float(input("\033[34mDigite a largura do terreno: \033[m"))
        comprimento = float(input("\033[34mDigite o comprimento do terreno: \033[m"))
        if largura <= 0 or comprimento <= 0:
            print("\033[31mValor inválido! Digite um número real positivo!\033[m")
            continue
        if largura > 0 and comprimento > 0:
            medida = área(largura, comprimento)
            print(f"\033[35mA área do terreno é: {medida:.2f}m² \033[m")
        while True:
            try:
                escolha = str(input("\033[34mQuer continuar? [S/N]: \033[m")).strip().upper()[0]
                if escolha not in "SN":
                    print("\033[31mOpção inválida! Digite somente S ou N.\033[m")
                    continue
                if escolha in "SN":
                    break
            except IndexError:
                print("\033[31mSua escolha não pode ficar vazia! Digite S ou N.\033[m")
                continue
        if escolha == "N":
            break
    except ValueError:
        print("\033[31mDigite apenas números reais.\033[m")
        continue