
contador = 0
while True:
    try:
        número = int(input("Digite um número inteiro para ver a sua tabuada (digite um número"
                            "negativo para parar): "))
        if número < 0:
            break
        contador += 1
        for i in range(1, 11):
            if i < 10:
                print(f"{número} x 0{i} = {i * número}")
            else:
                print(f"{número} x {i} = {i * número}")
    except ValueError:
        print("Valor inválido. Digite um número inteiro maior que zero.")
        continue
if contador == 1:
    plural = "número"
else:
    plural = "números"
print(f"Ao todo, você viu a tabuada de {contador} {plural}")