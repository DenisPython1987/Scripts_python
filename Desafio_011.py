altura = float(input('Qual a altura da parede em metros: '))
largura = float(input('Qual a largura da parede em metros: '))
area = altura * largura
tinta = area / 2

print(f'Você consegue pintar a parede inteira com {tinta:.2f} litros de tinta.')