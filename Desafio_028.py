from random import randint
from time import sleep

num = randint(0, 5)
print("Pensando em um número de 0 a 5")
sleep(3)

chute = int(input("Tente adivinhar o número (entre 0 e 5): "))

if chute == num:
    print("Parabéns! Você acertou!")
else:
    print("Que pena! Você errou!")
