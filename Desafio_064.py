soma = 0
cont = 0
número = 0
while True:
    número = int(input("Digite um número (999 para parar): "))
    if número == 999:
        break
    cont += 1
    soma += número
print(f"Foram digitados {cont} números e a soma deles é {soma}.")