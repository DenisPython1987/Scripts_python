import random

alunos = []

for i in range(4):
    alunos.append(str(input("Digite o nome do aluno: ")))

print(f"Os alunos escolhidos foram: {random.choices(alunos, k=5)}")
