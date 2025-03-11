#HERNÁNDEZ HERNÁNDEZ AARÓN
#3CV4

def comb_l(digitos):
    if not digitos:
        return []
    
    mapeo = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
    }

    def anexo(indice, camino):
        if indice == len(digitos):
            resultado.append("".join(camino))
            return
        
        for letra in mapeo[digitos[indice]]:
            anexo(indice + 1, camino + [letra])

    resultado = []
    anexo(0, [])
    return resultado

digitos = input("Ingrese los digitos (2-9): ").strip()

if digitos == "":
    print([])
else:
    if not digitos.isdigit() or any(d not in "23456789" for d in digitos):
        print("Solo se permiten los numeros del 2 al 9.")
    else:
        print("Combinaciones posibles:", comb_l(digitos))