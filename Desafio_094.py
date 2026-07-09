povo = list()
pessoa = dict()
soma_idade = contador = 0
while True:
    nome = str(input("Digite o nome da pessoa: ")).strip().title()
    pessoa["nome"] = nome
    while True:
        sexo = str(input("Digite o sexo da pessoa [M/F]: ")).strip().upper()[0]
        if sexo not in "MF":
            print("Digite somente M ou F.")
            continue
        if sexo in "MF":
            pessoa["sexo"] = sexo
            break
    while True:
        try:
            idade = int(input("Digite a idade da pessoa: "))
            if idade < 0 or idade > 120:
                print("A idade não pode ser negativa nem maior que 120 anos.")
                continue
            if 0 <= idade <= 120:
                pessoa["idade"] = idade
                soma_idade += idade
                break
        except ValueError:
            print("Dado inválido! Digite um número inteiro.")
            continue
    while True:
        escolha = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]
        if escolha not in "SN":
            print("Digite somente S ou N.")
            continue
        if escolha in "SN":
            break
    povo.append(pessoa.copy())
    pessoa.clear()
    if escolha in "S":
        continue
    elif escolha in "N":
        break

média = soma_idade / len(povo)
if len(povo) == 1:
    plural = "pessoa"
else:
    plural = "pessoas"
print(f"Ao todo foram cadastradas {len(povo)} {plural}.")
print(f"A média de idade das pessoas cadastradas é de {média}.")
print(f"Ao todo, tivemos: ", end='')
for pessoa in povo:
    contador += 1
    for chave, valor in pessoa.items():
        if chave == "sexo" and valor == "F":
            print(f"{pessoa['nome']}", end='')
            if contador == len(povo):
                print(", ", end='')
            elif contador == len(povo) - 1:
                print(" e ", end='')
            elif contador < len(povo) - 2:
                print(", ", end='')
if contador == 1:
    print("de mulher cadastrada.")
else:
    print("de mulheres cadastradas.")