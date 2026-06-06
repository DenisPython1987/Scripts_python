a = float(input("Digite o primeiro segmento: "))
b = float(input('Digite o segundo segmento: '))
c = float(input("Digite o terceiro segmento: "))

if a + b > c and a + c > b and b + c > a:
    print("Os seguimentos informados formam um triângulo!")
    if a == b == c:
        print("E formam um triangulo EQUILÁTERO!")
    elif a == b or b == c or a == c:
        print("E formam um triângulo ISÓSCELES!")
    else:
        print("E formam um triângulo ESCALENO!")
else:
    print("Os segmentos informado não formam um triângulo!")