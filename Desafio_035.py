a = int(input("Digite o primeiro lado do triângulo: "))
b = int(input("Digite o segundo lado: "))
c = int(input("Digite o terceiro lado: "))

if a + b > c and b + c > a and c + a > b:
    print("Os valores informados formam um triângulo!")
else:
    print("Os valores informados não formam um triângulo!")