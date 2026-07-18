def continuar():
    while True:
        try:
            escolha = str(input("\033[m\033[34mQuer ver a ajudar de outro comando? "
                                "[S/N]: \033[m")).strip().upper()[0]
            if escolha not in "SN":
                print("\033[31mOpção inválida! Digite somente S ou N.\033[m")
                continue
            if escolha in "SN":
                return escolha
        except IndexError:
            print("\033[31mOpção inválida! Digite somente S ou N.\033[m")
            continue


while True:
    help(input("\033[36mDigite o comando para o qual você quer ajuda: \033[m\033[35m"))
    escolha_principal = continuar()
    if escolha_principal == "N":
        break