cinquenta = vinte = dez = um = resto_50 = resto_20 = resto_10 = 0
saudação = "BANCO DO VIVAN"
print("-*-" * 20)
print(f"{saudação:^60}")
print("-*-" * 20)
while True:
    try:
        saque = int(input("Qual é o valor do saque?"))
        if saque <= 0:
            print(f"Valor inválido, tente novamente.")
            continue
        else:
            if saque // 50 > 0:
                cinquenta = saque // 50
                resto_50 = saque % 50
            if saque // 20 > 0:
                vinte = resto_50 // 20
                resto_20 = resto_50 % 20
            if saque // 10 > 0:
                dez = resto_20 // 10
                resto_10 = saque % 10
            if saque > 0:
                um = resto_10
            break
    except ValueError:
        print("Só são permitidos valores inteiros.")
        continue

print("-*-" * 20)
print(f"Você receberá seus R${saque} em notas de: ")
if cinquenta > 0:
    if cinquenta == 1:
        plural = "nota"
    else:
        plural = "notas"
    print(f"{cinquenta} {plural} de R$50,00")
if vinte > 0:
    if vinte == 1:
        plural = "nota"
    else:
        plural = "notas"
    print(f"{vinte} {plural} de R$20,00")
if dez > 0:
    if dez == 1:
        plural = "nota"
    else:
        plural = "notas"
    print(f"{dez} {plural} de R$10,00")
if um > 0:
    if um == 1:
        plural = "nota"
    else:
        plural = "notas"
    print(f"e {um} {plural} de R$1,00")
print("Obrigado! Volte sempre!")
print("-*-" * 20)
