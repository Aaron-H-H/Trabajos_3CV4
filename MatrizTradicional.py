#HERNÁNDEZ HERNÁNDEZ AARÓN
#3CV4
import time
import random

def generar_matriz(n):
    return [[random.random() for _ in range(n)] for _ in range(n)]

def multiplicar(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

if __name__ == "__main__":
    for n in [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]:
        A = generar_matriz(n)
        B = generar_matriz(n)
        
        inicio = time.time()
        C = multiplicar(A, B)
        tiempo = time.time() - inicio
        
        print(f"n={n}: {tiempo:.6f} segundos")
