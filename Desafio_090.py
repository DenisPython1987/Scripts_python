aluno = dict()
situação = ''

saudação = "Registro de média do aluno"
print("\033[36m-*-\033[m" * 20)
print(f"\033[36m{saudação:-^60}\033[m")
print("\033[36m-*-\033[m" * 20)
aluno['nome'] = str(input("\033[33mDigite o nome do aluno: \033[m")).strip().title()
print('\033[34m-\033[m' * 60)
while True:
    try:
        aluno['média'] = float(input("\033[33mDigite a média do aluno: \033[m"))
        if 0 <= aluno['média'] <= 10:
            break
        if 0 > aluno['média'] or aluno['média'] > 10:
            aluno['média'] = float(input("\033[31mDado inválido! Digite uma média enter 0 e 10: \033[m"))
            if 0 <= aluno['média'] <= 10:
                break
    except ValueError:
        aluno['média'] = float(input("\033[31mDado inválido! Digite uma média entre 0 e 10: \033[m"))
        if 0 <= aluno['média'] <= 10:
            break

print("\033[34m-\033[m" * 60)
if aluno['média'] < 7:
    situação = "\033[31mREPROVADO\033[m"
elif aluno['média'] < 9:
    situação = "\033[32mAPROVADO\033[m"
else:
    situação = "\033[32mAPROVADO COM LOUVOR\033[m"

print(f"O aluno {aluno['nome']} tem a média {aluno['média']} e está {situação}.")
despedida = "Fim do programa!"
print("\033[36m-*-\033[m" * 20)
print(f"\033[36m{despedida:-^60}\033[m")
print("\033[36m-*-\033[m" * 20)