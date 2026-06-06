preco = float(input("Qual é o preço do produto? R$"))

print("1 - À vista no dinheiro/cheque\n"
      "2 - À vista no cartão\n"
      "3 - Em até 2x no cartão\n"
      "4 - 3x ou mais no cartão")

condicao = int(input("Qual é a condição de pagamento? "))

if condicao == 1:
    preco = preco * 0.9
    print(f"Você vai pagar: R${preco:.2f}")