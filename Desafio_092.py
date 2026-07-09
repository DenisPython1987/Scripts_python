from datetime import date


pessoa = dict()
ano_atual = date.today().year

nome = str(input("Digite o nome da pessoa: ")).strip().title()
pessoa['nome'] = nome

while True:
    try:
        ano_nascimento = int(input("Digite o ano de nascimento: "))
        idade = ano_atual - ano_nascimento
        if idade > 1:
            pessoa['idade'] = idade
            break
        if idade < 1:
            print("O ano não pode estar no futuro")
            continue
    except ValueError:
        print("O ano deve ser uma data válida. Tente novamente.")
        continue

print(pessoa)

while True:
    try:
        ctps = int(input("Digite o número da Carteira de Trabalho: "))
        if ctps < 0:
            print("O número da Carteira de Trabalho não pode ser negativo. Tente novamente.")
            continue
        elif ctps == 0:
            pessoa['ctps'] = ctps
            break
        elif ctps > 0:
            pessoa['ctps'] = ctps
            while True:
                try:
                    ano_contratação = int(input("Digite o ano em que a pessoa foi contratada: "))
                    tempo_serviço = ano_atual - ano_contratação
                    if tempo_serviço < 0:
                        print("O ano não pode estar no futuro. Tente novamente.")
                        continue
                    else:
                        pessoa['ano de contratação'] = ano_contratação
                        
    except ValueError:
        print("O número da Carteira de Trabalho deve ser um número inteiro. Tente novamente.")
        continue