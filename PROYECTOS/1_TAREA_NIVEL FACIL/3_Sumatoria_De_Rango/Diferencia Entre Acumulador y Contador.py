contador = 0
acumulador = 0

for numero in range(1, 51):
    contador += 1      # Siempre suma 1
    acumulador += numero  # Suma el número actual

print(f"Contador (cantidad de números): {contador}")  # 50
print(f"Acumulador (suma total): {acumulador}")        # 1275


# Suma = n × (n + 1) ÷ 2
# Suma = 50 × 51 ÷ 2
# Suma = 2550 ÷ 2
# Suma = 1275 ✅