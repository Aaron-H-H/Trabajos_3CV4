#Hernandez Hernandez Aaron
#3CV4
def sumar_quimica(skill):
    skill_total = sum(skill)
    n = len(skill)
    if skill_total % (n // 2) != 0:
        return -1
    
    res = skill_total // (n // 2)
    skill.sort()
    quimica = 0
    izquierda = 0
    derecha = n - 1
    Equipos = [] 
    
    while izquierda < derecha:
        if skill[izquierda] + skill[derecha] != res:
            return -1

        Equipos.append((skill[izquierda], skill[derecha]))

        quimica += skill[izquierda] * skill[derecha]
        izquierda += 1
        derecha -= 1
    
    print("Equipos:")
    for team in Equipos:
        print(f"Equipo: {team[0]} y {team[1]} (Quimica: {team[0] * team[1]})")
    
    return quimica

datos = input("Ingresa las skills de los jugadores (separadas por espacios): ")
skill = list(map(int, datos.split()))

result = sumar_quimica(skill)
if result != -1:
    print("Quimica total:", result)
else:
    print("-1")