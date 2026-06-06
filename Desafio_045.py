from random import choice

escolhas_comp = ["papel", "pedra", "tesoura"]

jogada_comp = choice(escolhas_comp)

jokenpo = "\033[35mJokenpô\033[m"
print("\033[35m=*=\033[m" * 20)
print(f"{jokenpo:^60}")
print("\033[35m=*=\033[m" * 20)

print("\033[7;97mEscolha o que você vai jogar!\033[m")
print("\033[34m1 = papel")
print("2 = pedra")
print("3 = tesoura\033[m")
escolha = int(input("\033[32mQual é a sua escolha? \033[m"))

escolha_usuario = ''
if escolha == 1:
    escolha_usuario = "papel"
elif escolha == 2:
    escolha_usuario = "pedra"
elif escolha == 3:
    escolha_usuario = "tesoura"

if (escolha_usuario == "papel" and jogada_comp == "pedra" or escolha_usuario == "pedra" and
        jogada_comp == "tesoura") or escolha_usuario == "tesoura" and jogada_comp == "papel":
    print(f"\033[31mVocê escolheu '{escolha_usuario}' e eu escolhi '{jogada_comp}'\033[m")
    print("\033[35mVocê ganhou!\033[m")

elif (escolha_usuario == "pedra" and jogada_comp == "papel" or escolha_usuario == "tesoura" and
      jogada_comp == "pedra") or escolha_usuario == "papel" and jogada_comp == "tesoura":
    print(f"\033[31mVocê escolheu '{escolha_usuario}' e eu escolhi '{jogada_comp}'\033[m")
    print("\033[35mVocê perdeu!\033[m")

else:
    print(f"\033[31mVocê escolheu '{escolha_usuario}' e eu escolhi '{jogada_comp}'\033[m")
    print("\033[35mEmpate!\033[m")