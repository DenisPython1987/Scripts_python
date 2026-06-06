from datetime import date

ano_nasc = int(input("Digite o ano de nascimento: "))

hoje = date.today().year
idade = hoje - ano_nasc

if idade < 18:
    tempo = 18 - idade
    print(f"Você ainda não tem que se apresentar para o serviço militar.\n"
          f"Faltam {tempo} anos.")
elif idade == 18:
    print("Você está na idade de se apresentar ao serviço militar.")
else:
    tempo = idade - 18
    print(f"Você já deveria ter se apresentado. Passaram-se {tempo} anos.")
