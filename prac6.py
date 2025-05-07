# Hernandez Hernandez Aaron
# 3CV4
import math

def es_primo(n):
    if n <= 1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0: return False
    return True

def generar_fibonacci_filtrado(K):
    fib = [0, 1]
    pos = 2

    while True:
        siguiente = fib[-1] + fib[-2]
        if siguiente > K:
            break
        if not es_primo(pos):
            fib.append(siguiente)
        pos += 1

    fib_filtrado = [fib[i] for i in range(len(fib)) if not es_primo(i)]
    return sorted(list(set(fib_filtrado)), reverse=True)

def encontrar_terminos_minimos(K):
    fib_filtrado = generar_fibonacci_filtrado(K)
    contador = 0
    resto = K
    combinacion = []

    for num in fib_filtrado:
        if num <= resto:
            resto -= num
            contador += 1
            combinacion.append(num)
        if resto == 0:
            break
    return contador, combinacion

dia = 12
mes = 2
anio = 2003
K = (dia * 100) + (mes * 10) + (anio % 100)

print(f"Valor de K calculado: {K}")

fib_filtrado = generar_fibonacci_filtrado(K)
print("\nSecuencia Fibonacci filtrada (sin posiciones primas):")
print(fib_filtrado)

min_terminos, combinacion = encontrar_terminos_minimos(K)
print(f"\nNúmero mínimo de términos: {min_terminos}")
print("Combinación óptima:", " + ".join(map(str, combinacion)), "=", sum(combinacion))


