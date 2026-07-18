from datetime import date

def verifica_int():
    while True:
        try:
            ano = int(input("\033[36mDigite o ano de nascimento: \033[m"))
            atual = date.today().year
            if atual < ano:
                print("\033[31mO ano não pode estar no futuro.\033[m")
                continue
            if ano <= atual:
                return ano
            break
        except ValueError:
            print("\033[31mAno inválido. Digite o ano com quatro números inteiros.\033[m")
            continue


def voto(ano):
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return "\033[31mNEGADO\033[m"
    elif 16 <= idade < 18 or idade > 65:
        return "\033[31mOPCIONAL\033[m"
    else:
        return "\033[31mOBRIGATÓRIO\033[m"

atual = date.today().year
ano_nascimento = verifica_int()
idade = atual - ano_nascimento
print(f"\033[36mPara a idade de {idade} anos, o voto é \033[m{voto(ano_nascimento)}")