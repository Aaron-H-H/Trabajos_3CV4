#Hernández Hernández Aarón
def dividir(dividendo: int, divisor: int) -> int:
    if dividendo == -2**31 and divisor == -1:
        return 2**31 - 1  # Evitar desbordamiento
    # signo
    negativo = (dividendo < 0) != (divisor < 0)

    # valores absolutos
    dividendo, divisor = abs(dividendo), abs(divisor)
    cociente = 0
    
    while dividendo >= divisor:
        divisor_temporal, contador = divisor, 1
        while dividendo >= (divisor_temporal << 1):
            divisor_temporal <<= 1  
            contador <<= 1  
        dividendo -= divisor_temporal
        cociente += contador

    # Aplicar el signo al resultado
    if negativo:
        cociente = -cociente
    return min(max(cociente, -2**31), 2**31 - 1)

if __name__ == "__main__":
    dividendo = int(input("Ingrese el dividendo: "))
    divisor = int(input("Ingrese el divisor: "))
    resultado = dividir(dividendo, divisor)
    print(f"El resultado de la división es: {resultado}")