matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(3):
    for j in range(3):
        matriz[i][j] = (int(input(f"Digite um valor para [{i}, {j}]: ")))

for k in range(len(matriz)):
    for l in range(len(matriz[k])):
        print(f"[{matriz[k][l]}]", end=' ')
        if (l + 1) % 3 == 0:
            print("\n")