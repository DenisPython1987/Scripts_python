frase = str(input("Digite uma frase para saber se é um palíndromo: ")).strip().lower()
palavras = frase.split()
junto = ''.join(palavras)
inverso = []
for letra in range(len(junto) - 1, -1, -1):
    inverso.append(junto[letra])

final = ''.join(inverso)
if junto == final:
    print(f'A frase "{frase}" é um palíndromo!')
else:
    print(f'A frase "{frase}" não é um palíndromo!')