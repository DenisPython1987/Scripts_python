esquerda = direita = contador = 0

frase = str(input("Digite uma expressão com parênteses: ")).strip().upper()
while contador < len(frase):
    frase = str(input("Digite uma expressão com parênteses: ")).strip().upper()
    if "()" in frase:
        contador += 1
        for caractere in frase:
            if caractere == "(":
                esquerda += 1
                for parêntese in frase:
                    if parêntese == ")":
                        direita += 1
                        break

    else:
        print("Digite uma frase com parênteses! Tente novamente.")
        continue

if esquerda == direita:
    print("A frase digitada é uma experessão válida")
else:
    print("A frase digitada não é uma expressão válida")