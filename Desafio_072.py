números_extenso = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete",
           "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze",
           "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

número_usuário = 0

while True:
    try:
        número_usuário = int(input("Digite um número entre 0 e 20: "))
        if número_usuário < 0 or número_usuário > 20:
            print("Número inválido. Tente novamente.")
            continue
        if 0 <= número_usuário <= 20:
            break
    except ValueError:
        print("Opção inválida. Tente novamente.")
        continue

print(f"Você digitou o número {número_usuário} ou, por extenso, {números_extenso[número_usuário]}.")
