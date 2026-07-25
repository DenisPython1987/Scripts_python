def escolha():
    while True:
        try:
            opção = int(input("\033[36mQual é a sua opção: \033[m"))
            if opção <= 0 or opção >= 4:
                print("\033[31mOpção inválida! Digite um número entre 1 e 3.\033[m")
                continue
            if 1 <= opção <= 3:
                return opção
        except (ValueError, TypeError):
            print("\033[31mSua opção deve ser um número inteiro entre 1 e 3.\033[m")
            continue