matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = soma_3a_coluna = maior = 0
for i in range(3):
    for j in range(3):
        matriz[i][j] = (int(input(f"Digite um valor para [{i}, {j}]: ")))

for k in range(len(matriz)):
    for l in range(len(matriz[k])):
        print(f"[{matriz[k][l]}]", end=' ')
        if (l + 1) % 3 == 0:
            print("\n")
        if matriz[k][l] % 2 == 0:
            soma_pares += matriz[k][l]
        if l == 2:
            soma_3a_coluna += matriz[k][l]
        if matriz[1][l] > maior:
            maior = matriz[1][l]

print(f"A soma de todos os valores pares é: {soma_pares}.")
print(f"A soma de todos os valores da terceira coluna é: {soma_3a_coluna}.")
print(f"O maior número da segunda linha é: {maior}.")