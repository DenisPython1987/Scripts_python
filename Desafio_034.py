salario = float(input("Digite o salário do funcionário: "))

if salario <= 1250:
    novo_salario = salario + (salario * 1.15)
else:
    novo_salario = salario + (salario * 1.10)

print(f"O novo salário é {novo_salario:.2f}")
