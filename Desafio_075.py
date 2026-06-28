contador_9 = 0
valores_pares = tuple()
valores = (int(input("Digite um valor: ")),
           int(input("Digite um valor: ")),
           int(input("Digite um valor: ")),
           int(input("Digite um valor: ")))

for i in valores:
    if i == 9:
        contador_9 += 1
    if i % 2 == 0:
        par = str(i)
        valores_pares = valores_pares + (par, )
if contador_9 == 0:
    print("Não foi digitado o número 9.")
else:
    print(f"O número 9 apareceu {contador_9} vezes.")
try:
    print(f"O número 3 apareceu na {valores.index(3) + 1}ª posição.")
except ValueError:
    print("O número 3 não foi digitado.")

print("Foram digitados os seguintes valores pares: ", end=' ')
for i in range(0, len(valores_pares)):
    print(valores_pares[i], end='')
    if i < len(valores_pares) - 1:
        print(', ', end='')
    else:
        print('.')