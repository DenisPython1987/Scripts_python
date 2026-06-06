from datetime import date

ano_nasc = int(input("Digite o ano de nascimento: "))

idade = date.today().year - ano_nasc

if idade <= 9:
    print("Categoria: MIRIM")
elif idade <= 14:
    print("Categoria: INFANTIL")
elif idade <= 19:
    print("Categoria: JUNIOR")
elif idade <= 20:
    print("Categoria: SENIOR")
else:
    print('Categoria: MASTER')
