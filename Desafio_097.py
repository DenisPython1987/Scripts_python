

def escreva(texto):
    print("\033[35m~" * len(texto) + '~~\033[m')
    print(f"\033[36m {texto} \033[m")
    print("\033[35m~" * len(texto) + '~~\033[m')

escreva("Vivan DEV")
print()
escreva("Curso em Vídeo")
print()
escreva("Denisander Vivan")