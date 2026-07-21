from UtilidadesCeV.moeda import resumo
from UtilidadesCeV.dado import leia_dinheiro

número = leia_dinheiro("Digite o preço R$")
resumo(número, 15, 13)