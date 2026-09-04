def aumentar(valor: float, porcentagem: float) -> float:
    """Função para aumentar um valor com base num percentual. Retorna um float.
    Parâmetro valor: float que será aumentado.
    Parâmetro porcentagem: float que será o percentual de aumento."""
    return valor + (valor * porcentagem / 100)

def diminuir(valor: float, porcentagem: float) -> float:
    """Função para diminuir um valor com base em um percentual. Retorna um float.
    Parâmetro valor: float que será diminuído.
    Parâmetro porcentagem: float que será o percentual de decremento."""
    return valor - (valor * porcentagem / 100)

def dobro(valor: float):
    """Função que dobra um valor. Retorna um float.
    Parâmetro valor: float que será dobrado."""
    return valor * 2

def metade(valor: float) -> float:
    """Função que diminui um valor pela metade. Retorna um float.
    Parâmetro valor: float que será diminuído."""
    return valor / 2

def moeda(valor: float) -> str:
    """Função que retorna um valor float no formato de moeda brasileira. Retorna uma string.
    Parâmetro valor: float que será processado."""
    return f'R${valor:.2f}'.replace('.', ',')