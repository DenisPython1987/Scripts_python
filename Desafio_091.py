from operator import itemgetter
from random import randint
from time import sleep
contador = 1
jogadores = dict()
nomes = ("Jogador_1", "Jogador_2", "Jogador_3", "Jogador_4")
cores = ("\033[36m", "\033[35m", "\033[34m", "\033[33m", "\033[32m", "\033[31m")
for i in range(0, 4):
    jogo = randint(1, 6)
    jogadores[nomes[i]] = jogo
jogos_ordenados = dict(sorted(jogadores.items(), key=itemgetter(1), reverse=True))

for chave, valor in jogos_ordenados.items():
    cor = randint(0, 5)
    print(f"{cores[cor]}O {chave} tirou {valor} e está em {contador}º lugar.\033[m")
    sleep(1)
    contador += 1