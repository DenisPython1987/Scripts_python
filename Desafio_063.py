número = int(input("Digite um número: "))
contador = 1
primeiro = 1
segundo = 1
terceiro = 1

print("0 -> ", end='')
while contador <= número:
    print(primeiro, end=' ')
    if contador <= número - 1:
        print("-> ", end='')
    primeiro = segundo
    segundo = terceiro
    terceiro = primeiro + segundo
    contador += 1
