velocidade = int(input("Qual é a velocidade do carro? "))

multa = (velocidade - 80) * 7

if velocidade > 80:
    print(f"Você foi multado em R${multa}")

