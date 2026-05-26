num = int(input("Digite um número entre 0 e 9999: "))

milhar = num // 1000
centenas = num // 100 % 10
dezenas = num // 10 % 10
unidades = num // 1 % 10

print(f"O número {milhar} é a milhar")
print(f"O número {centenas} é a centena")
print(f"O número {dezenas} é a dezena")
print(f"O número {unidades} é a unidade")
