nome = str(input("Digite seu nome completo: ")).strip()

print(nome.upper())
print(nome.lower())
print(f"Ao todo, o seu nome tem {len(nome) - nome.count(" ")} letras")
nome = nome.split()
print(f"O seu primeiro nome tem {len(nome[0])} letras")

