from random import randint
from time import sleep

soma = 0
computador = randint(0, 10)

saudação = '\033[36mJOGO DE ADVINHAÇÃO\033[m'
print("\033[36m-*-\033[m" * 20)
print(f"{saudação:^60}")
print("\033[36m-*-\033[m" * 20)
print("\033[35mVou pensar em um número entre 0 e 10")
sleep(1)
print("Pensando", end='')
sleep(1)
print(".", end='')
sleep(1)
print('.', end='')
sleep(1)
print(".\033[m")
while True:
    palpite = int(input("\033[32mQual é o seu palpite? \033[m"))
    if palpite == computador:
        soma += 1
        print(f"\033[32mParabéns!!! Eu pensei no número {computador}.")
        print(f"Você precisou de {soma} tentativas.\033[m")
        break
    elif palpite < 0 or palpite > 10:
        soma += 1
        print(f"\033[31mO número {palpite} não está no intervalo entre 0 e 10. Tente novamente.\033[m")
        continue
    elif palpite < computador:
        soma += 1
        print(f"\033[31mÉ mais que {palpite}.\033[m")
        continue
    elif palpite > computador:
        soma += 1
        print(f"\033[31mÉ menos que {palpite}.\033[m")
        continue