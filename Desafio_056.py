
idade_maior = 0
cont_mulheres = 0
nome_maior = ''
maior = 0
soma = 0
sexo_opção = ''
for i in range(1, 5):
    nome = str(input("Digite o nome da pessoa: ")).strip().title()
    idade = int(input("Digte a idade da pessoa: "))
    if idade < 1 or idade > 120:
        print("Idade inválida. Tente novamente.")
        continue
    else:
        soma += idade
        if idade > maior:
            maior = idade
    sexo = int(input("Digite 1 para homem ou 2 para mulher: "))
    if sexo == 1:
        sexo_opção = "homem"
        if sexo == 1 and idade == maior:
            nome_maior = nome
            idade_maior = idade
    elif sexo == 2:
        sexo_opção = "mulher"
        if sexo_opção == "mulher" and idade < 20:
            cont_mulheres += 1
    else:
        print("Opção inválida. Tente novamente.")
        continue
média = soma / 4
print(f"A média de idade do grupo é: {média:.2f} anos.")
print(f"O homem mais velho é o {nome_maior} com {idade_maior} anos.")
print(f"Ao todo, temos {cont_mulheres} mulheres com menos de 20 anos.")