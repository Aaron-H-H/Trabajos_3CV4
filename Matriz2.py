#HERNÁNDEZ HERNÁNDEZ AARÓN
#3CV4
import time
import random

def generar_matriz(n):
    return [[random.random() for _ in range(n)] for _ in range(n)]

def sumar(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A))] for i in range(len(A))]

def multiplicar(A, B):
    n = len(A)
    if n <= 64:  
        return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    
    m = n // 2
    # Dividir matrices en submatrices
    A11 = [fila[:m] for fila in A[:m]]
    A12 = [fila[m:] for fila in A[:m]]
    A21 = [fila[:m] for fila in A[m:]]
    A22 = [fila[m:] for fila in A[m:]]
    
    B11 = [fila[:m] for fila in B[:m]]
    B12 = [fila[m:] for fila in B[:m]]
    B21 = [fila[:m] for fila in B[m:]]
    B22 = [fila[m:] for fila in B[m:]]
    
    C11 = sumar(multiplicar(A11, B11), multiplicar(A12, B21))
    C12 = sumar(multiplicar(A11, B12), multiplicar(A12, B22))
    C21 = sumar(multiplicar(A21, B11), multiplicar(A22, B21))
    C22 = sumar(multiplicar(A21, B12), multiplicar(A22, B22))
    
    return [C11[i] + C12[i] for i in range(m)] + [C21[i] + C22[i] for i in range(m)]

if __name__ == "__main__":
    for n in [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]:
        A = generar_matriz(n)
        B = generar_matriz(n)
        
        inicio = time.time()
        C = multiplicar(A, B)
        tiempo = time.time() - inicio
        
        print(f"n={n}: {tiempo:.6f} segundos")