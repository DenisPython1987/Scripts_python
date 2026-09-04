import moeda

#Pedindo um preço ao usuário e guardando na variável 'número'
número = float(input("Digite o preço R$"))

#Pedindobum percentual ao usuário e guardando na variável 'percentual'
percentual = float(input("Digite a porcentagem: "))

#Mostrando o resultado da função aumentar() passando o número e o percentual como parâmetros
print(f"O preço de {número} aumentado em {percentual}% é {moeda.aumentar(número, percentual)}.")

#Mostrando o resultado da função diminuir() passando número e percentual como parâmetros
print(f"O preço de {número} diminuído em {percentual}% é {moeda.diminuir(número, percentual)}.")

#Mostrando o resultado da função dobro() passando número como parâmetro
print(f"O dobro de {número} é {moeda.dobro(número)}.")

#Mostrando o resultado da função metade() passando número como parâmetro 
print(f"A metade de {número} é {moeda.metade(número)}.")