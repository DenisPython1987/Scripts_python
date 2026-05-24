import random

alunos = []

for i in range(1, 5):
    nome = str(input("Digite o nome do aluno: "))
    alunos.append(nome)

print(f"O aluno escolhido foi: {random.choice(alunos)}")
 