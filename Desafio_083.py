# Esse daqui eu desisti de fazer porque eu não dei conta

esquerda = direita = 0

frase = str(input("Digite uma expressão com parênteses: ")).strip().upper()
for posição, caractere in enumerate(frase):
    if caractere == "(":
        esquerda += 1
        for parêntese in frase[posição:]:
            if parêntese == ")":
                direita += 1
                break

if esquerda == direita:
    print("A frase digitada é uma experessão válida")
else:
    print("A frase digitada não é uma expressão válida")