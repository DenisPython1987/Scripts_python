preco = float(input("Qual é o preço do produto? R$"))

print("1 - À vista no dinheiro/cheque\n"
      "2 - À vista no cartão\n"
      "3 - Em até 2x no cartão\n"
      "4 - 3x ou mais no cartão")

condicao = int(input("Qual é a condição de pagamento? "))

if condicao == 1:
    preco = preco * 0.9
    print(f"Você vai pagar: R${preco:.2f}")
elif condicao == 2:
    preco = preco * 0.95
    print(f"Você vai pagar: R${preco:.2f}")
elif condicao == 3:
    preco = preco / 2
    print(f"Você vai pagar duas parcelas de R${preco:.2f}")
elif condicao == 4:
    parcelas = int(input("Quantas parcelas? "))
    preco = preco * 1.2
    preco_parc = preco / parcelas
    print(f"Você vai pagar um total de R${preco:.2f} em {parcelas} parcelas de R${preco_parc:.2f}.")
