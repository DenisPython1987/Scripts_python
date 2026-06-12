maior = 0
menor = 0

for i in range(1, 6):
    peso = float(input("Digite o peso: "))

    if peso > maior:
        maior = peso
    if peso < menor or i == 1:
        menor = peso

print(f"O maior peso foi de {maior:.2f}kg e o menor foi de {menor:.2f}kg")