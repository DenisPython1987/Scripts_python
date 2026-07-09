from datetime import date
from time import sleep

pessoa = dict()
ano_atual = date.today().year
aposentar = False
tempo_aposentar = 35
tempo_serviço = 0
idade = 0
ctps = 0

saudação = '  CADASTRO DE TRABALHADOR  '
print("\033[36m-*-\033[m" * 20)
print(f'\033[36m{saudação:-^60}\033[m')
print("\033[36m-*-\033[m" * 20)
print()
nome = str(input("\033[32mDigite o nome da pessoa: \033[m")).strip().title()
pessoa['nome'] = nome

while True:
    try:
        ano_nascimento = int(input("\033[32mDigite o ano de nascimento: \033[m"))
        idade = ano_atual - ano_nascimento
        if idade > 1:
            pessoa['idade'] = idade
            break
        if idade < 1:
            print("\033[31mO ano não pode estar no futuro\033[m")
            continue
    except ValueError:
        print("\033[31mO ano deve ser uma data válida. Tente novamente.\033[m")
        continue

while True:
    try:
        ctps = int(input("\033[32mDigite o número da Carteira de Trabalho: \033[m"))
        if ctps < 0:
            print("\033[31mO número da Carteira de Trabalho não pode ser negativo. Tente novamente.\033[m")
            continue
        elif ctps == 0:
            pessoa['ctps'] = ctps
            break
        elif ctps > 0:
            pessoa['ctps'] = ctps
            while True:
                try:
                    ano_contratação = int(input("\033[32mDigite o ano em que a "
                                                "pessoa foi contratada: \033[m"))
                    tempo_serviço = ano_atual - ano_contratação
                    tempo_aposentar = 35 - tempo_serviço
                    if tempo_serviço < 0:
                        print("\033[31mO ano não pode estar no futuro. Tente novamente.\033[m")
                        continue
                    else:
                        pessoa['ano de contratação'] = ano_contratação
                    if tempo_aposentar <= 0:
                        aposentar = True
                    else:
                        pessoa['aposentar'] = tempo_aposentar
                    break
                except ValueError:
                    print("\033[31mDigite um ano válido. Tente novamente.\033[m")
                    continue
            break
    except ValueError:
        print("\033[31mO número da Carteira de Trabalho"
              " deve ser um número inteiro. Tente novamente.\033[m")
        continue

apresentação = "  APRESENTAÇÃO DO CADASTRO  "
print("\033[36m-*-\033[m" * 20)
print(f"\033[36m{apresentação:-^60}\033[m")
print("\033[36m-*-\033[m" * 20)

for chave, valor in pessoa.items():
    if chave == 'nome':
        print(f"\033[35mO seu nome é {valor}\033[m")
        sleep(1)
    elif chave == 'idade':
        print(f"\033[35mSua idade é de {valor}\033[m")
        sleep(1)
    elif chave == 'ctps':
        if ctps == 0:
            print("\033[35mVocê ainda não tem experiência profissional!\033[m")
            sleep(1)
        else:
            print(f"\033[35mO número da sua Carteira de Trabalho é {valor}\033[m")
            sleep(1)
    elif chave == 'ano de contratação':
        print(f"\033[35mVocê foi contratado em {valor}\033[m")
        sleep(1)

if ctps > 0:
    if aposentar:
        print("\033[35mVocê já pode se aposentar\033[m")
        sleep(1)
    elif not aposentar:
        print(f"\033[35mAinda faltam {pessoa['aposentar']} anos para você se aposentar.\033[m")
        sleep(1)

despedida = "  OBRIGADO POR USAR NOSSO PROGRAMA  "
print("\033[36m-*-\033[m" * 20)
print(f"\033[36m{despedida:-^60}\033[m")
print("\033[36m-*-\033[m" * 20)