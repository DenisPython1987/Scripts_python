def aumentar(valor: float, porcentagem: float) -> float:
    """Função para aumentar um valor com base em um percentual. Retorna um float.
    Parâmetro valor: float que será aumentado.
    Parâmetro porcentagem: float que representa o percentual de aumento"""
    return valor + (valor * porcentagem / 100)

def diminuir(valor: float, porcentagem: float) -> float:
    """Função para diminuir um valor com base num percentual. Retorna um float.
    Parâmetro valor: float que será diminuído.
    Parâmetro percentual: float que representa o percentual a ser diminuído."""
    return valor - (valor * porcentagem / 100)

def dobro(valor: float) -> float:
    """Função para dobrar um valor. Pode retornar um int ou um float, conforme a entrada.
    Parâmetro valor: float que será dobrado."""
    return valor * 2

def metade(valor: float) -> float:
    """Função para dividir um número pela metade. Retorna sempre um float.
    Parâmetro valor: float que será dividido."""
    return valor / 2