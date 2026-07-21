import moeda

número = float(input("Digite o preço R$"))
percentual = float(input("Digite a porcentagem do aumento: "))
print(f"O preço de {número} aumentado em {percentual}% é {moeda.aumentar(número, percentual)}.")
print(f"O preço de {número} diminuído em {percentual}% é {moeda.diminuir(número, percentual)}.")
print(f"O dobro de {número} é {moeda.dobro(número)}.")
print(f"A metade de {número} é {moeda.metade(número)}.")