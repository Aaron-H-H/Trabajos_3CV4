#Hernandez Hernandez Aaron
#3CV4
# Problema de la mochila
items = [
    {"name": "Guitarra", "weight": 1, "value": 1500},
    {"name": "Laptop",   "weight": 3, "value": 2000},
    {"name": "Estéreo",  "weight": 4, "value": 3000},
    {"name": "iPhone",   "weight": 1, "value": 2000}
]

capacity = 4 
n = len(items)

dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
track = [["" for _ in range(capacity + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for w in range(1, capacity + 1):
        item = items[i-1]
        if item["weight"] <= w:
            value_with = item["value"] + dp[i-1][w - item["weight"]]
            value_without = dp[i-1][w]

            if value_with > value_without:
                dp[i][w] = value_with
                track[i][w] = (track[i-1][w - item["weight"]] + item["name"] + ", ").strip()
            else:
                dp[i][w] = value_without
                track[i][w] = track[i-1][w]
        else:
            dp[i][w] = dp[i-1][w]
            track[i][w] = track[i-1][w]

def print_table(title, data, headers):
    print(f"\n{title}")
    print("-" * (15 + 20 * len(headers)))
    print(f"{'Objeto':<15}", end="")
    for h in headers:
        print(f"{h:^20}", end="")
    print()
    print("-" * (15 + 20 * len(headers)))
    for i in range(1, len(data)):
        print(f"{items[i-1]['name']:<15}", end="")
        for j in range(1, len(data[i])):
            print(f"{str(data[i][j]):^20}", end="")
        print()
    print("-" * (15 + 20 * len(headers)))

headers = [f"{w} lb" for w in range(1, capacity + 1)]
print_table("VALORES MÁXIMOS POR CAPACIDAD", dp, headers)
print_table("OBJETOS SELECCIONADOS POR CAPACIDAD", track, headers)
print("\nRESULTADO FINAL")
print("=" * 40)
print(f"Capacidad máxima: {capacity} lb")
print(f"Valor máximo posible: ${dp[n][capacity]}")
print(f"Objetos seleccionados: {track[n][capacity]}")
