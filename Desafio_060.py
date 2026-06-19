número = int(input("Digite um número para ver seu fatorial: "))
contador = número
soma = 1
while contador > 0:
    soma *= contador
    contador -= 1

print(f"O fatorial de {número} é {soma}.")
