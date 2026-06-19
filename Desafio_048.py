soma = 0
for i in range(1, 501):
    if i % 3 == 0 and i % 2 == 1:
        soma += i
print(f"A soma dos números múltiplos de 3 entre 1 e 500 é: {soma}")