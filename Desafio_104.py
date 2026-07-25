

def leia_int():
    while True:
        try:
            número = int(input("\033[36mDigite um número inteiro: \033[m"))
            return número
        except (ValueError, TypeError):
            print("\033[31mDado inválido! Digite apenas um número inteiro!\033[m")
            continue


valor = leia_int()
print(f"\033[35mO número digitado foi \033[31m{valor}\033[m")