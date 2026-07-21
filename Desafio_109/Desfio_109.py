import moeda

número = float(input("Digite o preço R$"))
percentual = float(input("Digite a porcentagem: "))
print(f"O preço de {moeda.moeda(número)} aumentado "
      f"em {percentual}% é {moeda.aumentar(número, percentual, True)}.")
print(f"O preço de {moeda.moeda(número)} diminuído "
      f"em {percentual}% é {moeda.diminuir(número, percentual, True)}.")
print(f"O dobro de {moeda.moeda(número)} é {moeda.dobro(número, False)}.")
print(f"A metade de {moeda.moeda(número)} é {moeda.metade(número, False)}.")