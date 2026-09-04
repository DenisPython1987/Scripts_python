def aumentar(valor: int, porcentagem: float) -> float:
    """Função para aumentar um valor com base em um percentual. Retorna um float.
    Parâmetro valor: int ou float que será aumentado.
    Parâmetro porcentagem: float que representa o percentual de aumento"""
    return valor + (valor * porcentagem / 100)

def diminuir(valor: int, porcentagem: float) -> float:
    """Função para diminuir um valor com base num percentual. Retorna um float.
    Parâmetro valor: inteiro ou float que será diminuído.
    Parâmetro percentual: float que representa o percentual a ser diminuído."""
    return valor - (valor * porcentagem / 100)

def dobro(valor: int) -> int:
    """Função para dobrar um valor. Pode retornar um int ou um float, conforme a entrada.
    Parâmetro valor: int ou float que será dobrado."""
    return valor * 2

def metade(valor: int) -> float:
    """Função para dividir um número pela metade. Retorna sempre um float.
    Parâmetro valor: int ou float que será dividido."""
    return valor / 2