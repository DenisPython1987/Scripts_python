alunos = list()
parcial_1 = list()
parcial_2 = list()

saucação = "ESCOLA VIVANI"
print("-*-" * 20)
print(f"{saucação:^60}")
print("-*-" * 20)

while True:
    parcial_1.append(str(input("Qual é o nome do aluno? ")).strip().title())
    while True:
        try:
            parcial_2.append(float(input("Digite a 1ª nota: ")))
            parcial_2.append(float(input("Digite a 2ª nota: ")))
            if parcial_2[0] < 0 or parcial_2[0] > 10 or parcial_2[1] < 0 or parcial_2[1] > 10:
                print("Dado inválido. Digite um número real entre 0.00 e 10.00.")
                continue
            else:
                parcial_1.append(parcial_2[:])
                alunos.append(parcial_1[:])
                parcial_1.clear()
                parcial_2.clear()
                break
        except ValueError:
            print("Dado inválido. Digite um número real entre 0.00 e 10.00.")
            continue
    while True:
        escolha = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]
        if escolha not in "SN":
            print("Opção inválida! Digite apenas S ou N.")
            continue
        if escolha in "SN":
            break
    if escolha == "N":
        break

while True:
    print("-*-" * 20)
    legenda_1 = "Média"
    legenda_2 = "Aluno"
    legenda_3 = "Número"
    print(f"{legenda_3:-<5}  {legenda_2:.<20} = {legenda_1}")
    for indice in range(0, len(alunos)):
        média = (alunos[indice][1][0] + alunos[indice][1][1]) / 2
        print(f"# {indice + 1:-<5} {alunos[indice][0]:.<20} = {média:.2f} #")
    print("-*-" * 20)
    while True:
        try:
            opção = int(input("Deseja ver as notas de qual aluno "
                          "[digite o número do aluno desejado]: "))
            if opção < 0 or opção > len(alunos):
                print("Opção inválida. Digite o número do aluno desejado.")
                continue
            else:
                print(f"As notas do aluno {alunos[opção - 1][0]} são: {alunos[opção - 1][1][0]}"
                      f"e {alunos[opção - 1][1][1]}")
                break
        except ValueError:
            print("Opção inválida. Digite o número do aluno desejado.")
            continue
    while True:
        escolha_2 = str(input("Deseja ver as notas de mais algum aluno? [S/N]: ")).strip().upper()[0]
        if escolha_2 not in "SN":
            print("Opção inválida. Digite apenas S ou N.")
            continue
        elif escolha_2 in "SN":
            break
    if escolha_2 == "N":
        break

despedida = "Obrigado por utilizar os nosso serviços"
print("-*-" * 20)
print(f"{despedida:^60}")
print("-*-" * 20)