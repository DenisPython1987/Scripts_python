distancia = float(input("Qual é a distância da viagem: "))

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print(f"Sua viagem fica em R${preco:.2f}")
