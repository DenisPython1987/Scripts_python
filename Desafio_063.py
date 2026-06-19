número = int(input("Digite um número: "))
contador = 1
primeiro = 1
segundo = 1
terceiro = 1

while contador <= número:
    print(primeiro, end=' ')
    primeiro = segundo
    segundo = terceiro
    terceiro = primeiro + segundo
    contador += 1
