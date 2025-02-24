"""
Hernández Hernández Aarón
3CV4
"""
def es_palindromo(x: int) -> bool:
    if x < 0:
        return False
    if x == 0:
        return True

    normal = x
    reverso = 0

    while x > 0:
        digito = x % 10
        reverso = reverso * 10 + digito
        x = x // 10
    return normal == reverso

def main():
    print("---- Palíndromos ----")
    
    while True:
        while True:
            try:
                x = int(input("Ingresa un número entero: "))
                break  
            except ValueError:
                print("Coloca un valor correcto")

        if es_palindromo(x):
            print(f"Sí, {x} es palíndromo.")
        else:
            print(f"No, {x} no es palíndromo.")

        while True:
            continuar = input("¿Deseas probar otro número? (y/n): ").lower()
            if continuar in ("y", "n"):
                break
            print("Opción no válida.")

        if continuar == "n":
            print("Finalizado.")
            print(" (•_•) ")
            print("<)   )╯")
            print(" /   \\ ")
            break

if __name__ == "__main__":
    main()

