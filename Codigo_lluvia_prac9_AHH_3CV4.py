#Hernandez Hernandez Aaron
#3CV4
def atrapar_agua(lluvia):
    if not lluvia:
        return 0

    n = len(lluvia)
    max_izq = [0] * n
    max_der = [0] * n

    max_izq[0] = lluvia[0]
    for i in range(1, n):
        max_izq[i] = max(max_izq[i - 1], lluvia[i])

    max_der[n - 1] = lluvia[n - 1]
    for i in range(n - 2, -1, -1):
        max_der[i] = max(max_der[i + 1], lluvia[i])

    agua = 0
    for i in range(n):
        agua += min(max_izq[i], max_der[i]) - lluvia[i]

    return agua

entrada = input("Ingresa los valores separados por comas (ejemplo: 0,1,0,2,1,0,1,3,2,1,2,1): ")
lluvia = list(map(int, entrada.split(',')))

print("Agua atrapada:", atrapar_agua(lluvia))
