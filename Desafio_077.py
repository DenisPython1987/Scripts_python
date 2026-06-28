palavras = ("abacaxi", "abacate", "panela", "colher", "computador", "curso", "mouse", "papel", "aleluia")
for i in range(0, len(palavras)):
    print(f"A palavra {palavras[i]} tem as seguintes vogais:", end=' ')
    for j in range(0, len(palavras[i])):
        if palavras[i][j] in "aeiou":
            print(palavras[i][j], end='')
            if j < len(palavras[i]) - 1:
                print(", ", end='')
    print(".\n")