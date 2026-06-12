from datetime import date

cont_maiores = 0
cont_menores = 0
hoje = date.today().year

for i in range(1, 8):
    data_aniversário = int(input("Digite o ano de nascimento: "))
    if (hoje - data_aniversário) <= 21:
        cont_menores += 1
    elif (hoje - data_aniversário) > 21:
        cont_maiores += 1

print(f"Temos {cont_maiores} pessoas maiores de idade.")
print(f"Temos {cont_menores} pessoas menores de idade.")
