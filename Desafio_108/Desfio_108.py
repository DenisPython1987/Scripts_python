import moeda

número = float(input("Digite o preço R$"))
percentual = float(input("Digite a porcentagem: "))
print(f"O preço de {moeda.moeda(número)} aumentado "
      f"em {percentual}% é {moeda.moeda(moeda.aumentar(número, percentual))}.")
print(f"O preço de {moeda.moeda(número)} diminuído "
      f"em {percentual}% é {moeda.moeda(moeda.diminuir(número, percentual))}.")
print(f"O dobro de {moeda.moeda(número)} é {moeda.moeda(moeda.dobro(número))}.")
print(f"A metade de {moeda.moeda(número)} é {moeda.moeda(moeda.metade(número))}.")