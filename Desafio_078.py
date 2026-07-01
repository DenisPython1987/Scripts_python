números = list()
posição_maior = posição_menor = menor = maior = contador = 0

while contador < 5:
    try:
        valor = int(input(f"Digite o {contador + 1}º valor: "))
        if isinstance(valor, int):
            números.append(valor)
            contador += 1
    except (ValueError, TypeError):
        print("O valor digitado é inválido. Tente novamente.")
        continue

for i, j in enumerate(números):
    if i == 0:
        maior = menor = j
        posição_menor = posição_maior = i
    else:
        if j > maior:
            maior = j
            posição_maior = i
        if j < menor:
            menor = j
            posição_menor = i

print(f"O maior número foi {maior} e está na {posição_maior + 1}ª posição.")
print(f"O menor número foi {menor} e está na {posição_menor + 1}ª posição.")