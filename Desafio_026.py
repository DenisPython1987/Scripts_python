frase = str(input("Digite uma frase qualquer: "))

print(f"A sua frase contém {frase.count('a')} letras A")
print(f"A primeira ocorrência da letra A na sua frase é no índice {frase.find('a') + 1}")
print(f"A última ocorrência da letra A na sua frase é no índice {frase.rfind('a') + 1}")
