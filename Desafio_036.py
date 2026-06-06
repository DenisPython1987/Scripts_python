casa = float(input("Qual o valor da casa? R$"))
salario = float(input("Qual é o salário do comprador? R$"))
anos = int(input("Em quantos anos será pago? "))

meses = anos * 12
prestacao = casa / meses

if prestacao > salario * 0.3:
    print("Você não tem salário suficiente para financiar essa casa!")
else:
    print(f"Você irá pagar a casa de R${casa:.2f}, em {anos} anos,\n"
          f" com a prestação no valor de R${prestacao:.2f}")
