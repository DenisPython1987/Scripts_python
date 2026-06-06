nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2

if media < 5:
    print("Aluno REPROVADO!")
elif media >= 5 and media <= 6.9:
    print("Aluno em RECUPERAÇÃO")
else:
    print("Aluno APROVADO!")
