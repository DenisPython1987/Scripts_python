from random import randint

números = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
maior = 0
menor = 0

for i in range(0, 5):
    if i == 0:
        maior = números[i]
        menor = números[i]
    else:
        if maior > números[i]:
            maior = números[i]
        if menor < números[i]:
            menor = números[i]

print(f"Os números sorteador foram: {números}.")
print(f"O maior número foi: {maior}.")
print(f"O menor número foi: {menor}.")
