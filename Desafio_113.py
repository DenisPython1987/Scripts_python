def leia_int(mensagem):
    while True:
        valor = 0
        try:
            valor = int(input(mensagem))
        except (ValueError, TypeError):
            print(f"{valor} não é um número inteiro válido. Tente novamente.")
            continue
        except KeyboardInterrupt:
            print("O usuário não quis digitar esse valor.")
            break
        else:
            return valor

def leia_float(mensagem):
    while True:
        valor = 0
        try:
            valor = float(input(mensagem))
        except (ValueError, TypeError):
            print(f"{valor} não é um número real válido. Tente novamente.")
            continue
        except KeyboardInterrupt:
            print("O usuário não quis digitar esse valor.")
            break
        else:
            return valor

valor_1 = leia_int("Digite um valor inteiro: ")
valor_2 = leia_float("Digite um valor real: ")
print(f"Você digitou os valores {valor_1} e {valor_2}")