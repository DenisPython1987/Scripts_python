nome = str(input("Digite um nome: ")).strip()

if 'silva' in nome.lower():
    print(f"A pessoa chamada de {nome} tem Silva em seu nome")
else:
    print(f"A pessoa chamada de {nome} não tem Silva em seu nome")