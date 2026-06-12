print('-*-' * 15)
número = int(input("Digite um número para ver a tabuada: "))
print("-*-" * 15)

for i in range(1, 11):
    print(f"{i} x {número} = {i * número}")
