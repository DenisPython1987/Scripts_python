opção = 0
numero1 = 0
numero2 = 0

while True:
    if opção == 0 or opção == 4:
        numero1 = int(input("Digite o primeiro número: "))
        numero2 = int(input("Digite o segundo número: "))
    print("""
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa""")
    opção = int(input("Qual é a sua opção? "))
    if opção < 1 or opção > 5:
        print("Opção inválida. Digite uma opção entre 1 e 5.")
        continue
    elif opção == 1:
        soma = numero1 + numero2
        print(f"A soma entre {numero1} e {numero2} é {soma}")
        continue
    elif opção == 2:
        multiplicar = numero1 * numero2
        print(f"A multiplicação entre {numero1} e {numero2} é {multiplicar}")
        continue
    elif opção == 3:
        if numero1 > numero2:
            print(f"O número {numero1} é maior que {numero2}")
            continue
        else:
            print(f"O número {numero2} é maior que {numero1}")
            continue
    elif opção == 5:
        print("Obrigado por usar nossa calculadora! Até breve...")
        break