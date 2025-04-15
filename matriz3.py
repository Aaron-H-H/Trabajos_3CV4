#HERNÁNDEZ HERNÁNDEZ AARÓN
#3CV4
import time
import random

def generar_matriz(n):
    return [[random.random() for _ in range(n)] for _ in range(n)]

def sumar(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A))] for i in range(len(A))]

def restar(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A))] for i in range(len(A))]

def multiplicar(A, B):
    n = len(A)
    if n <= 64:
        return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    
    m = n // 2
    A11 = [fila[:m] for fila in A[:m]]
    A12 = [fila[m:] for fila in A[:m]]
    A21 = [fila[:m] for fila in A[m:]]
    A22 = [fila[m:] for fila in A[m:]]
    
    B11 = [fila[:m] for fila in B[:m]]
    B12 = [fila[m:] for fila in B[:m]]
    B21 = [fila[:m] for fila in B[m:]]
    B22 = [fila[m:] for fila in B[m:]]
    
    M1 = multiplicar(sumar(A11, A22), sumar(B11, B22))
    M2 = multiplicar(sumar(A21, A22), B11)
    M3 = multiplicar(A11, restar(B12, B22))
    M4 = multiplicar(A22, restar(B21, B11))
    M5 = multiplicar(sumar(A11, A12), B22)
    M6 = multiplicar(restar(A21, A11), sumar(B11, B12))
    M7 = multiplicar(restar(A12, A22), sumar(B21, B22))
    
    C11 = sumar(restar(sumar(M1, M4), M5), M7)
    C12 = sumar(M3, M5)
    C21 = sumar(M2, M4)
    C22 = sumar(restar(sumar(M1, M3), M2), M6)
    
    return [C11[i] + C12[i] for i in range(m)] + [C21[i] + C22[i] for i in range(m)]

if __name__ == "__main__":
    for n in [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]:
        A = generar_matriz(n)
        B = generar_matriz(n)
        
        inicio = time.time()
        C = multiplicar(A, B)
        tiempo = time.time() - inicio
        
        print(f"n={n}: {tiempo:.6f} segundos")