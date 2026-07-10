#Eu não consegui consertar o bug da continuação dos prints


from time import sleep

povo = list()
mulheres = list()
pessoa = dict()
soma_idade = contador = 0

def print_cores(mensagen, end=None):
    from random import randint
    cores = ("\033[31m", "\033[32m", "\033[33m", "\033[34m", "\033[35m", "\033[36m", "\033[97m")
    número = randint(0, 6)
    print(f"{cores[número]}{mensagen}\033[m")

saudação = "CADASTRO DE PESSOAS"
print_cores("-*-" * 20)
print_cores(f"{saudação:^60}")
print_cores("-*-" * 20)
while True:
    nome = str(input("\033[34mDigite o nome da pessoa: \033[m")).strip().title()
    pessoa["nome"] = nome
    while True:
        try:
            sexo = str(input("\033[35mDigite o sexo da pessoa [M/F]: \033[m")).strip().upper()[0]
            if sexo not in "MF":
                print_cores("Digite somente M ou F.")
                continue
            if sexo == "F":
                mulheres.append(pessoa["nome"])
            if sexo in "MF":
                pessoa["sexo"] = sexo
                break
        except IndexError:
            print_cores("O nome não pode estar vazio.")
            continue
    while True:
        try:
            idade = int(input("\033[31mDigite a idade da pessoa: \033[m"))
            if idade < 0 or idade > 120:
                print_cores("A idade não pode ser negativa nem maior que 120 anos.")
                continue
            if 0 <= idade <= 120:
                pessoa["idade"] = idade
                soma_idade += idade
                break
        except ValueError:
            print_cores("Dado inválido! Digite um número inteiro.")
            continue
    while True:
        escolha = str(input("\033[33mDeseja continuar? [S/N]: \033[m")).strip().upper()[0]
        if escolha not in "SN":
            print_cores("Digite somente S ou N.")
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

print()
estatísticas = "ESTATÍSTICAS"
print_cores("-=-" * 20)
print_cores(f"{estatísticas:^60}")
print_cores("-=-" * 20)

print_cores("PROCESSANDO", end='')
sleep(1)
for i in range(0, 2):
    print_cores(".", end='')
    sleep(1)
print()

if len(povo) == 1:
    plural = "pessoa"
else:
    plural = "pessoas"
print_cores(f"Ao todo foram cadastradas {len(povo)} {plural}.")
sleep(1)
print_cores(f"A média de idade das pessoas cadastradas é de {média:.2f}.")
sleep(1)
print_cores(f"Ao todo, tivemos: ", end='')
sleep(1)
for indice, mulher in enumerate(mulheres):
    print_cores(f"{mulher}", end='')
    sleep(1)
    if indice == len(mulheres) - 1:
        print_cores(", ", end='')
    elif indice == len(mulheres) - 2:
        print_cores(" e ", end='')
    elif indice < len(mulheres) - 2:
        print_cores(", ", end='')
if contador == 1:
    print_cores("de mulher cadastrada.")
else:
    print_cores("de mulheres cadastradas.")

print_cores("As seguinte pessoas tem idade acima da média:")
sleep(1)
for pessoa in povo:
    if pessoa["idade"] > média:
        print_cores(f"{pessoa['nome']} com {pessoa['idade']} anos.")
        sleep(1)

despedida = "VOLTE SEMPRE"
print_cores("-*-" * 20)
print_cores(f"{despedida:^60}")
print_cores("-*-" * 20)