import math

angulo = float(input("Digite um ângulo qualquer: "))

angulo_convertido = math.radians(angulo)

print(f"O seno de {angulo} é: {math.sin(angulo_convertido):.2f}")
print(f"O cosseno de {angulo} é: {math.cos(angulo_convertido):.2f}")
print(f"A tangente de {angulo} é: {math.tan(angulo_convertido):.2f}")
