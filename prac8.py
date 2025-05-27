def es_revuelta(cadena1: str, cadena2: str) -> bool:
    from functools import lru_cache
 
    @lru_cache(maxsize=None)
    def auxiliar(a: str, b: str) -> bool:
        if a == b:
            return True
        if sorted(a) != sorted(b):
            return False
 
        longitud = len(a)
        for i in range(1, longitud):
            if auxiliar(a[:i], b[:i]) and auxiliar(a[i:], b[i:]):
                return True
            if auxiliar(a[:i], b[-i:]) and auxiliar(a[i:], b[:-i]):
                return True
        return False
 
    return auxiliar(cadena1, cadena2)
 
while True:
    entrada1 = input("Ingresa la primera cadena (o escribe 'salir' para terminar): ")
    if entrada1.lower() == 'salir':
        break
    entrada2 = input("Ingresa la segunda cadena: ")
    resultado = es_revuelta(entrada1, entrada2)
    print(f"es_revuelta('{entrada1}', '{entrada2}') -> {resultado}\n")