a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

if a > b:
    print(f"O número {a} é maior que o número {b}.")
elif b > a:
    print(f"O número {b} é maior que o número {a}.")
else:
    print(f"Os números {a} e {b} são iguais.")