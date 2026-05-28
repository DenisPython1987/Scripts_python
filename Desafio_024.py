cidade = str(input("Informe o nome da cidade: ")).strip().lower()

if cidade[:5] == "santo":
    print(f"A cidade de {cidade.title()} tem nome de santo.")
else:
    print(f"A cidade de {cidade.title()} não tem nome de santo.")