while True:
    sexo = str(input("Informe o sexo [M/F]: ")).strip().upper()[0]
    if sexo not in "MmFf":
        print("Sexo inválido. Tente novamente.")
        continue
    elif sexo in "Mm":
        print("Sexo masculino registrado com sucesso.")
        break
    else:
        print("Sexo feminino registrado com sucesso.")
        break
