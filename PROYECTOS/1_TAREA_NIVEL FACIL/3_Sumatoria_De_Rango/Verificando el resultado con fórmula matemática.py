suma_total = 0

for numero in range(1, 51):
    suma_total += numero

# Fórmula matemática: suma = n * (n + 1) / 2
suma_formula = 50 * 51 // 2

print(f"Suma con bucle for: {suma_total}")
print(f"Suma con fórmula: {suma_formula}")
print(f"¿Son iguales? {suma_total == suma_formula}")