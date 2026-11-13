
def es_primo(numero: int, primos_conocidos: list[int]) -> bool:
    if numero == 2:
        return True
    for primo in primos_conocidos:
        if numero % primo == 0:
            return False
    return True

def generar_primos(valor_maximo: int) -> list[int]:

    primos = []
    candidatos = []

    # Generar lista de candidatos del 2 al valor máximo
    for i in range(2, valor_maximo + 1):
        candidatos.append(i)

    # Filtrar los primos usando el concepto de primalidad
    for candidato in candidatos:
        if es_primo(candidato, primos):
            primos.append(candidato)
    
    return primos