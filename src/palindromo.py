def es_palindromo(texto):
    """Verifica si un texto es un palíndromo (ignora mayúsculas y espacios)."""
    texto_limpio = ''.join(texto.lower().split())  # Eliminar espacios y pasar a minúsculas
    return texto_limpio == texto_limpio[::-1]
