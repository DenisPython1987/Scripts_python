número = int(input("\033[35mDigite um número para saber se é primo: \033[m"))
contador = 0

for i in range(1, número + 1):
    if número % i == 0:
        contador += 1

if contador == 2:
    print(f"\033[33mO número {número} é primo!\033[m")
else:
    print(f"\033[33mO número {número} não é primo!\033[m")