idade = soma = cont = maior_homem = maior_mulher = contador_idade_18 = menor_20 = homens = 0
cadastro = {}
homem_mais_velho = mulher_mais_velha = ""
while True:
    while True:
        nome = str(input("Digite o nome: ")).strip().lower()
        if nome.isdigit():
            print(f"{nome} não é um nome válido. Tente novamente.")
            continue
        elif not any(char.isalnum() for char in nome):
            print(f"{nome} não é um nome válido. Tente novamente!")
            continue
        elif nome in "@#$_&-+()/?!;:*£~|•√π÷×§∆\\}{=°^¥€¢%©®™✓[]<>":
            print("Seu nome não pode conter caracteres especiais. Digite um nome válido.")
            continue
        else:
            break

    while True:
        try:
            idade = int(input("Digite a idade: "))
            if idade < 0 or idade > 125:
                print("Idade inválida. Tente novamente!")
                continue
            if 0 < idade < 125:
                if idade > 18:
                    contador_idade_18 += 1
                soma += idade
                break
        except ValueError:
            print(f"{idade} não corresponde a uma idade válida. Tente novamente!")
            continue

    while True:
        sexo = str(input("Digite o sexo [M/F]: ")).strip().upper()[0]
        if sexo not in "MmFf":
            print("Sexo inválido. Tente novamente")
            continue
        if sexo in "MmFf":
            if sexo in "Mm":
                homens += 1
            break
    cadastro[nome] = {"nome": nome, "idade": idade, "sexo": sexo}
    cont += 1
    if cont == 1 and sexo in "Ff":
        maior_mulher = idade
        mulher_mais_velha = nome
    if cont == 1 and sexo in "Mm":
        maior_homem = idade
        homem_mais_velho = nome
    if idade > maior_mulher and sexo in "Ff":
        maior_mulher = idade
        mulher_mais_velha = nome
    if idade > maior_homem and sexo in "Mm":
        maior_homem = idade
        homem_mais_velho = nome
    if idade < 20 and sexo in "Ff":
        menor_20 += 1
    escolha = str(input("Você quer continuar? [S/N]: ")).strip().upper()[0]
    
    if escolha in "Nn":
        média = soma / cont
        break
if cont == 1:
    cadastro = "cadastro"
else:
    cadastro = "cadastros"

if homens == 1:
    homem = 'homem'
    cadastro_homem = "foi cadastrado"
else:
    homem = "homens"
    cadastro_homem = "foram cadastrados"

if menor_20 == 1:
    mulher = 'mulher menor'
else:
    mulher = "mulheres menores"

if contador_idade_18 == 1:
    pessoa = "pessoa maior"
else:
    pessoa = "pessoas maiores"

print(f"Ao todo, foram {cont} {cadastro}.")
print(f"A soma das idades é {soma} anos.")
print(f"A média de idade é de {média:.2f} anos.")
if maior_homem > 0:
    print(f"O homem mais velho tem {maior_homem} anos e se chama {homem_mais_velho.title()}.")
    print(f"Ao todo, {cadastro_homem} {homens} {homem}.")
else:
    print("Não foram cadastrados homens")
if maior_mulher > 0:
    print(f"A mulher mais velha tem {maior_mulher} anos e se chama {mulher_mais_velha.title()}.")
    print(f"Ao todo, temos {menor_20} {mulher} de 20 anos.")
else:
    print("Não foram cadastradas mulheres")
print(f"Ao todo, temos {contador_idade_18} {pessoa} de 18 anos.")

